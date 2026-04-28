from sklearn.metrics.pairwise import cosine_similarity
from vertexai.preview.language_models import TextEmbeddingModel

embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-004")

class VectorStore:
    def __init__(self):
        self.data = []

    def add(self, text, metadata):
        emb = embedding_model.get_embeddings([text])[0].values
        self.data.append((text, metadata, emb))

    def search(self, query, top_k=2):
        query_emb = embedding_model.get_embeddings([query])[0].values

        scored = []
        for text, metadata, emb in self.data:
            score = cosine_similarity([query_emb], [emb])[0][0]
            scored.append((score, text, metadata))

        # sort by best match
        scored.sort(reverse=True)

        return scored[:top_k]