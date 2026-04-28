from vertexai.generative_models import GenerativeModel
from vertexai.language_models import TextEmbeddingModel
from services.vertex_init import vertexai

# LLM
model = GenerativeModel("gemini-2.5-pro")


def ask_llm(prompt: str) -> str:
    response = model.generate_content(prompt)
    return response.text

# Embeddings
embed_model = TextEmbeddingModel.from_pretrained("text-embedding-004")

def get_embedding(text: str):
    return embed_model.get_embeddings([text])[0].values
