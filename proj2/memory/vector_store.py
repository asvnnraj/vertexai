from sklearn.metrics.pairwise import cosine_similarity
from vertexai.preview.language_models import TextEmbeddingModel

embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-004")

class VectorStore:
    def __init__(self):
        self.data = []

    def add(self, text, metadata):
        emb = embedding_model.get_embeddings([text])[0].values
        self.data.append((text, metadata, emb))

    def search(self, query):
        query_emb = embedding_model.get_embeddings([query])[0].values

        best = None
        best_score = -1

        for text, metadata, emb in self.data:
            score = cosine_similarity([query_emb], [emb])[0][0]
            if score > best_score:
                best_score = score
                best = (text, metadata)

        return best