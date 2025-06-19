from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os

def search_chroma(query: str, top_k=3):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1"
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
