
from agents.base_agent import BaseAgent
from tools.payment_tools import fetch_transaction

class InvestigationAgent(BaseAgent):

    def __init__(self, vector_store):
        super().__init__(
            name="InvestigationAgent",
            system_prompt="You investigate payment issues using tools and memory."
        )
        self.vector_store = vector_store

    def run(self, user_query):
        txn = fetch_transaction()

        memory = self.vector_store.search(txn["reason"])

        return {
            "query": user_query,
            "transaction": txn,
            "memory": memory
        }