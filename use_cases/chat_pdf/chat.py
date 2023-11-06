from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.chains import RetrievalQA

import streamlit as st
import pandas as pd
import os
import sys
import time
from loguru import logger

from libs.using_ffm import get_ffm, get_embed
from libs.misc_pdf import get_pdf_pages

logger.add(sys.stdout, backtrace=True, diagnose=True)


data_path = 'data/'
st.title('Chat with your own PDF')

# Reset the conversation
if "message" not in st.session_state:
    st.session_state.message = []
if "tmp_location" not in st.session_state:
    st.session_state.tmp_location = None


# Get the file pdf path from local
file_obj = st.sidebar.file_uploader("1. Upload PDF File", type=["pdf"])

if file_obj:
    logger.debug(f"file_path: {file_obj}")
    pages = get_pdf_pages(file_obj)
    logger.debug(f"pages: {pages}")

llm = get_ffm()

# # logger.debug(llm)
st.info(llm("You are a chatbot. Give me a simple greeting response for user who using this product. product name is called Formosa Foundation Model. Do not say too much. Just emoji as possible."))