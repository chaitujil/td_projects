from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('TeluguSBERT-STS')
embeddings = model.encode(sentences)
print(embeddings)