import streamlit as st
from loguru import logger

logger.add("file.log", rotation="500 MB")

st.title("TWCC ChatBot (Demo)")

container = st.container()


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def do_post(query):
    import requests

    url = 'http://127.0.0.1:8000/ask/'
    myobj = {'q': query}

    x = requests.post(url, json = myobj)
    logger.info("input: "+query)
    logger.info("answer: "+x.json()['answer'])
    
    return x.json()['answer']

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = do_post(f"{prompt}")
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})