import time
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import JSONLoader
from langchain.vectorstores import FAISS
from libs.using_ffm import get_embed

GENERATED_JSON_FILE_PATH = "/home/ubuntu/AFS_tools/use_cases/webcrawler_chatbot/scrapy/website/website/website.json"

embeddings_zh = get_embed()

splitFunc = RecursiveCharacterTextSplitter(separators='',
                                           chunk_size=250,
                                           chunk_overlap=20,
                                           length_function=len)

start_time = time.time()


def metadata_func(record: dict, metadata: dict) -> dict:
    metadata["url"] = record["url"]
    metadata["title"] = record["title"]
    return metadata


loader = JSONLoader(
    file_path=GENERATED_JSON_FILE_PATH,
    jq_schema='.[]',
    content_key="body",
    metadata_func=metadata_func,)

datasets = loader.load_and_split(text_splitter=splitFunc)

doc_embedding = FAISS.from_documents(
    documents=datasets, embedding=embeddings_zh)

doc_embedding.save_local(f"./embeddings/all_docs_embedding_website")

end_time = time.time()
running_time = end_time - start_time
print(f"Running time: {running_time} seconds")
print(f"FAISS vector store saved.")