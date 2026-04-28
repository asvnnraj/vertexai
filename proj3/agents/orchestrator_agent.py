from agents.investigation_agent import InvestigationAgent
from agents.resolution_agent import ResolutionAgent

class OrchestratorAgent:

    def __init__(self, vector_store):
        self.investigator = InvestigationAgent(vector_store)
        self.resolver = ResolutionAgent()

    def run(self, query):
        print("[Orchestrator] → Investigation Agent")
        context = self.investigator.run(query)

        print("[Orchestrator] → Resolution Agent")
        result = self.resolver.run(context)

        return result