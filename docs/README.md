# 🧠 RAG-Powered FAQ Chatbot (LangChain + Chroma + n8n)

### 🔗 Live Test Flow
```
POST /webhook/ask
  → query_chroma.py → ChromaDB
  → OpenRouter → LLM response
  → final_answer returned
```

### 📦 Requirements
```bash
pip install -r requirements.txt
```

### 🛠 Setup
1. Embed PDFs using `setup.py` 
2. Start n8n locally: `npx n8n`
3. Test using Postman:
```json
{
  "query": "What is RAG?"
}
```

### 🔐 Environment
Create `.env` from `.env.template`:
```env
OPENROUTER_API_KEY=org-xxxxxxxxxxxxxxxxxxxxxxxxx
```
