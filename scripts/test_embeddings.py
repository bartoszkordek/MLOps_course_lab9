import requests
import numpy as np

ALB_URL = "http://embeddings-alb-1657377824.us-east-1.elb.amazonaws.com"

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

response = requests.post(f"{ALB_URL}/embed", json={
    "inputs": [
        "machine learning model deployment",
        "deploying AI models to production",
        "how to bake a chocolate cake"
    ]
})

vectors = response.json()
print("Similar pair similarity:    ", cosine_similarity(vectors[0], vectors[1]))
print("Dissimilar pair similarity: ", cosine_similarity(vectors[0], vectors[2]))