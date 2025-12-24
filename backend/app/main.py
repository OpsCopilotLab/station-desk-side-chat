from fastapi import FastAPI

app = FastAPI(title="Station Desk-Side Chat (Demo)")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(q: str):
    # placeholder: later wire to retrieval + citations
    return {"answer": "Demo stub. RAG wiring next.", "citations": []}
