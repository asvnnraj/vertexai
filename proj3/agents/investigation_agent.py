from agents.base_agent import BaseAgent
from tools.payment_tools import fetch_transaction_history

class InvestigationAgent:

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def run(self, user_query):
        history = fetch_transaction_history()

        # Detect pattern
        reasons = [txn["reason"] for txn in history]
        most_common = max(set(reasons), key=reasons.count)

        # Memory (past issues)
        memory = self.vector_store.search(most_common, top_k=1)

        # RAG (knowledge base)
        knowledge = self.vector_store.search(user_query, top_k=2)

        return {
            "query": user_query,
            "history": history,
            "pattern": most_common,
            "memory": memory,
            "knowledge": knowledge
        }