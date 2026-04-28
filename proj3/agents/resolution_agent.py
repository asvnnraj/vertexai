from agents.base_agent import BaseAgent

class ResolutionAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="ResolutionAgent",
            system_prompt="You are a payment expert. Provide root cause and solution."
        )

    def run(self, context):
        prompt = f"""
        You are a senior payment expert.

        Analyze:
        - Transaction history
        - Failure pattern
        - Knowledge base insights

        Context:
        {context}

        Provide:
        1. Root cause (based on pattern)
        2. Why it is repeating
        3. Immediate fix
        4. Preventive steps
        5. Whether user should retry or not
        """

        return self.model.generate_content(prompt).text