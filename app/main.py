from fastapi import FastAPI, Request
from scripts.query_chroma import search_chroma

app = FastAPI()

@app.post("/ask")
async def ask(request: Request):
    body = await request.json()
    query = body.get("query", "")
    result = search_chroma(query)
    return {"chunks": result}