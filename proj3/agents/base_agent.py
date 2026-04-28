import vertexai
from vertexai.generative_models import GenerativeModel
from config import PROJECT_ID, LOCATION, MODEL_NAME

vertexai.init(project=PROJECT_ID, location=LOCATION)

class BaseAgent:
    def __init__(self, name, system_prompt, tools=None):
        self.name = name
        self.system_prompt = system_prompt
        self.model = GenerativeModel(MODEL_NAME)
        self.tools = tools or []

    def run(self, input_data):
        prompt = f"""
        System: {self.system_prompt}
        Input: {input_data}
        """

        response = self.model.generate_content(prompt)
        return response.text