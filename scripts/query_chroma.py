from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_community.vectorstores import Chroma
import os

def search_chroma(query: str, top_k=3):
    hf_token = os.getenv("HF_API_TOKEN")
    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key=hf_token,
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = Chroma(
        persist_directory="./chroma_store",
        embedding_function=embeddings
    )
    results = db.similarity_search_with_score(query, k=top_k)
    response = []
    for doc, score in results:
        response.append(f"Chunk:\n{doc.page_content}\nSimilarity: {score:.4f}\n")
    return "\n".join(response)
