
from pydantic import BaseModel
from agents.orchestrator_agent import OrchestratorAgent
from memory.vector_store import VectorStore
from memory.knowledge_base import documents
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


vector_store = VectorStore()


for doc in documents:
    vector_store.add(doc, metadata="kb")

vector_store.add("INSUFFICIENT_FUNDS", "Retry with sufficient balance")
vector_store.add("NETWORK_ERROR", "Retry after some time")

agent = OrchestratorAgent(vector_store)

class Request(BaseModel):
    message: str

@app.post("/chat")
def chat(req: Request):
    response = agent.run(req.message)
    return {"response": response}