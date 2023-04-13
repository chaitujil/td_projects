from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans


if __name__ == '__main__':

    corpus = [
        "రుచికరమైన టొమాటో గొజ్జు రిసిపి",
        "సీఎం కేసీఆర్‌పై ఎల్లలు దాటిన అభిమానం",
        "ఏపీలో స్థానిక ఎన్నికల కసరత్తు.. రేపు ఈసీ అఖిలపక్ష భేటీ",
        "నిరూపిస్తే నిమిషంలో రాజీనామా చేస్తా: కేసీఆర్‌",
        "బ్యాటింగ్‌లో కోహ్లీసేన అట్టర్ ఫ్లాఫ్.. హైదరాబాద్ ముందు ఈజీ టార్గెట్!",
        "ఏపీలో స్థానిక సంస్థ‌ల ఎన్నిక‌ల‌కు రాష్ట్ర ఎన్నిక‌ల సంఘం మొగ్గుచూపుతున్న క్ర‌మంలో",
        "అందుకే అతని బౌలింగ్ ఒకసారి ఆడాలనుకుంటున్నా: సచిన్ టెండూల్కర్",
        "కొత్త స్మార్ట్‌ఫోన్‌లు వచ్చేసాయి!!! ఫీచర్స్ బ్రహ్మాండం",
        "కోహ్లీసేనదే బ్యాటింగ్.. ఇరు జట్లలో మార్పులు!",
        "మరో రెండు కొత్త ఫోన్లు ? ధరలు మరియు ఫీచర్లు చూడండి.",
        "క్యాప్సికం మసాలా గ్రేవీ రిసిపి",
        "25 వేల లోపు ఈ స్మార్ట్‌ఫోన్‌ల మీద ఊహించని డిస్కౌంట్ ఆఫర్స్!",
        "సీఎం కేసీఆర్‌పై అభిమానానికి ఎల్లలు లేవు. తెలంగాణ సాధించిన",
        "రుచికరమైన కీమా దాళ్ రిసిపి: పరాఠా, చపాతీ, నాన్ మరియు రోటీలకు అద్భుతమైన కాంబినేషన్",
    ]

    model = SentenceTransformer('l3cube-pune/telugu-sentence-similarity-sbert')
    sentence_embeddings = model.encode(corpus)

    # k-means clustering
    number_of_clusters = 4
    kmeans_clusterer = KMeans(n_clusters=number_of_clusters)
    kmeans_clusterer.fit(sentence_embeddings)

    assigned_labels = kmeans_clusterer.labels_

    # initialize empty clusters
    clusters = [[] for i in range(number_of_clusters)]

    for sentence_id, cluster_id in enumerate(assigned_labels):
        clusters[cluster_id].append(corpus[sentence_id])

    for index, cluster in enumerate(clusters):
        print("Cluster ", index + 1)
        print(cluster)
        print("")