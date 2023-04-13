from sentence_transformers import SentenceTransformer

if __name__ == '__main__':
    sentences = [
        "ర్యాష్‌ డ్రైవింగ్‌ చేసిన సినీ నిర్మాతపై కేసు",
        "సరికొత్త వార్తా విశేషాలను పొందండి, విభాగాలను తీసివేయండి, అలాగే మీకు నచ్చిన మరిన్నిటిని ఎంచుకోండి"]
    model = SentenceTransformer('l3cube-pune/telugu-sentence-similarity-sbert')
    sentence_embeddings = model.encode(sentences)
    print(sentence_embeddings)
    print(sentence_embeddings.shape)

    print(sentence_embeddings[0])
