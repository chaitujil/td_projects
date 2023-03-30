from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('l3cube-pune/telugu-sentence-similarity-sbert')
embeddings = model.encode(sentences)
print(embeddings)
