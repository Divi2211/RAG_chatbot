# scripts/setup.py

import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load documents (both PDF and text)
def load_documents(directory: str):
    loaders = [
        DirectoryLoader(directory, glob="**/*.pdf", loader_cls=PyPDFLoader),
        DirectoryLoader(directory, glob="**/*.txt", loader_cls=TextLoader)
    ]
    documents = []
    for loader in loaders:
        documents.extend(loader.load())
    return documents

# Chunk docs
def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(documents)

# Use Hugging Face model like 'all-MiniLM-L6-v2'
def create_vectorstore(chunks, persist_directory="chroma_store"):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=persist_directory)
    vectordb.persist()
    print(f"✅ Vector DB created using Hugging Face at `{persist_directory}`.")

# Run
def main():
    documents = load_documents("../data/sample-documents")  # adjust if needed
    chunks = split_documents(documents)
    create_vectorstore(chunks)

if __name__ == "__main__":
    main()
