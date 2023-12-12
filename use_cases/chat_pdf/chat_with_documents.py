import os
import sys
import tempfile
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import ConversationalRetrievalChain

# from langchain.vectorstores import DocArrayInMemorySearch
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.prompts.prompt import PromptTemplate
from libs.using_ffm import get_ffm, get_embed
import logging


TEXT_CHUNK_SIZE = int(os.environ.get("TEXT_CHUNK_SIZE", 750))
TEXT_CHUNK_OVERLAP = int(os.environ.get("TEXT_CHUNK_OVERLAP", 0))
SEARCH_KWARGS_K = int(os.environ.get("SEARCH_KWARGS_K", 5))

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

@st.cache_resource(ttl="1h")
def configure_retriever(uploaded_files):
    # Read documents
    docs = []
    temp_dir = tempfile.TemporaryDirectory()
    for file in uploaded_files:
        temp_filepath = os.path.join(temp_dir.name, file.name)
        with open(temp_filepath, "wb") as f:
            f.write(file.getvalue())
        loader = PyPDFLoader(temp_filepath)
        docs.extend(loader.load())

    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=TEXT_CHUNK_SIZE, chunk_overlap=TEXT_CHUNK_OVERLAP)
    splits = text_splitter.split_documents(docs)

    # Create embeddings and store in vectordb
    # embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    embeddings = get_embed()
    doc_embedding = FAISS.from_documents(
        documents=splits, embedding=embeddings)
    doc_embedding.save_local(f"/tmp/all_docs_embedding_website")

    # vectordb = DocArrayInMemorySearch.from_documents(splits, embeddings)

    # Define retriever
    # retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={"k": 2, "fetch_k": 4})
    retriever = doc_embedding.as_retriever(search_type="mmr", search_kwargs={
                                           "k": SEARCH_KWARGS_K, "include_metadata": True})

    return retriever


class StreamHandler(BaseCallbackHandler):
    def __init__(self, container: st.delta_generator.DeltaGenerator, initial_text: str = ""):
        self.container = container
        self.text = initial_text
        self.run_id_ignore_token = None
        logger.info(f"{initial_text}")

    def on_llm_start(self, serialized: dict, prompts: list, **kwargs):
        # Workaround to prevent showing the rephrased question as output
        if prompts[0].startswith("Human"):
            self.run_id_ignore_token = kwargs.get("run_id")
            logger.info(f"{kwargs}")

    # def on_llm_new_token(self, token: str, **kwargs) -> None:
    #     if self.run_id_ignore_token == kwargs.get("run_id", False):
    #         return
    #     self.text += token
    #     self.container.markdown(self.text)

    def on_llm_end(self, response, **kwargs) -> None:
        """Run when LLM ends running."""
        self.container.markdown(response.generations[0][0].text)


class PrintRetrievalHandler(BaseCallbackHandler):
    def __init__(self, container):
        self.status = container.status("**Context Retrieval**")
        self.LLMManagerMixin = 1

    def on_retriever_start(self, serialized: dict, query: str, **kwargs):
        self.status.write(f"**Question:** {query}")
        self.status.update(label=f"**Context Retrieval:** {query}")

    def on_retriever_end(self, documents, **kwargs):
        for idx, doc in enumerate(documents):
            source = os.path.basename(doc.metadata["source"])
            self.status.write(f"**Document {idx} from {source}**")
            self.status.markdown(doc.page_content)
        self.status.update(state="complete")


# openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
# if not openai_api_key:
#     st.info("Please add your OpenAI API key to continue.")
#     st.stop()

uploaded_files = st.sidebar.file_uploader(
    label="Upload PDF files", type=["pdf"], accept_multiple_files=True
)
if not uploaded_files:
    st.info("Please upload PDF documents to continue.")
    st.stop()

retriever = configure_retriever(uploaded_files)

# Setup memory for contextual conversation
msgs = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(
    memory_key="chat_history", chat_memory=msgs, return_messages=True)

# Setup LLM and QA chain
# llm = ChatOpenAI(
#     model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, temperature=0, streaming=True
# )
llm = get_ffm()

custom_template = """Given the following conversation and a follow up question. Just fix typing error, do not rewrite question.
Translate in Traditional Chinese if possible.

對談歷史:
{{ {chat_history} }}

Follow Up Input: {{ {question} }}
Standalone question:
"""
CUSTOM_QUESTION_PROMPT = PromptTemplate.from_template(custom_template)


QA_PROMPT_DOCUMENT_CHAT = """
你是一個助理，請依據下面的資訊，回答問題。

{{
{context}
}}

Question: '{question}'
Answer:
"""
QA_PROMPT = PromptTemplate(
    input_variables=["context", "question"], template=QA_PROMPT_DOCUMENT_CHAT)


qa_chain = ConversationalRetrievalChain.from_llm(
    llm, retriever=retriever, memory=memory, verbose=True,
    combine_docs_chain_kwargs={'prompt': QA_PROMPT},
)

logger.info(f"QA chain: {qa_chain.combine_docs_chain.llm_chain.prompt}")


if len(msgs.messages) == 0 or st.sidebar.button("Clear message history"):
    msgs.clear()
    msgs.add_ai_message("How can I help you?")

avatars = {"human": "user", "ai": "assistant"}
for msg in msgs.messages:
    st.chat_message(avatars[msg.type]).write(msg.content)

if user_query := st.chat_input(placeholder="Ask me anything!"):
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        retrieval_handler = PrintRetrievalHandler(st.container())
        stream_handler = StreamHandler(st.empty())
        response = qa_chain.run(user_query, callbacks=[
                                retrieval_handler, stream_handler])
