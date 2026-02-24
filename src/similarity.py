from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import  cosine_similarity


model = SentenceTransformer('all-MiniLM-L6-v2')


def compute_similarity(text1,text2):
    embedding1 = model.encode(text1, normalize_embeddings=True)
    embedding2 = model.encode(text2, normalize_embeddings=True)
    
    score = cosine_similarity([embedding1], [embedding2])[0][0]
    score =score *  0.9
    return score