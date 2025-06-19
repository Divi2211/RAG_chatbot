## 🎯 Objective
Build a production-ready FAQ chatbot using Retrieval-Augmented Generation (RAG).

## 📐 Stack
- LangChain (Python)
- ChromaDB (vector store)
- Hugging Face Embeddings
- OpenRouter (LLM)
- n8n (orchestration)

## 🔁 Workflow
1. Webhook → Accepts query
2. Python script → Searches ChromaDB
3. HTTP node → Sends context + query to OpenRouter
4. Set node → Extracts assistant message
5. Webhook response → Sends back answer

## 🧪 Test Cases
Located in `tests/sample-queries.json`
