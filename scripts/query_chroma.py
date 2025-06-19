# scripts/query_chroma.py
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
def search_chroma(query: str, top_k=3):
    # Load persisted DB
    db = Chroma(persist_directory="../chroma_store", embedding_function=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))
    # Perform search
    results = db.similarity_search_with_score(query, k=top_k)
    # Format response
    response = []
    for doc, score in results:
        response.append({
            "chunk": doc.page_content,
            "similarity": score
        })

    return response
# Example usage
if __name__ == "__main__":
    test_query = "What is RAG?"
    result = search_chroma(test_query)
    print(" Top Results:")
    for r in result:
        print(f"\n Chunk:\n{r['chunk']}\n Similarity: {r['similarity']:.4f}")
