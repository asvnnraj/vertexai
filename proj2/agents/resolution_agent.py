from agents.base_agent import BaseAgent

class ResolutionAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="ResolutionAgent",
            system_prompt="You are a payment expert. Provide root cause and solution."
        )

    def run(self, context):
        return super().run(context)