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
from PyPDF2 import PdfReader, PdfWriter



data_path = 'data/'
st.write('Powered by TWCC FFM LLAMA2 Model-7B')

# Reset the conversation
if "message" not in st.session_state:
    st.session_state.message = []
if "tmp_location" not in st.session_state:
    st.session_state.tmp_location = None


# Get the file pdf path from local
file_path = st.sidebar.file_uploader("Upload PDF File", type=["pdf"])

