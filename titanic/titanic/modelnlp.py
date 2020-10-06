def predict(opinion):
    import pickle
    import nltk
    from sklearn.feature_extraction.text import TfidfVectorizer
    from nltk.corpus import stopwords
    #from sklearn.externals import joblib

    x=[opinion]
    c=[opinion]
    sentiment=pickle.load(open('sentiment.sav','rb'))
    vectorizer = TfidfVectorizer(max_features=20, min_df=0.3, max_df=1.0, stop_words=stopwords.words('english'))
    vector = sentiment.vectorizer.fit_transform(x).toarray()
    vec = vectorizer.transform(c).toarray()

    prediction=sentiment.predict(vec)

    if prediction!=None:

        prediction="Sentiment is " + prediction

    else:
        prediction='error'
    return prediction
