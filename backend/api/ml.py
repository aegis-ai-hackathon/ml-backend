import pickle
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
def predict():
    corpus = pickle.load(open(r"api\textcorpus.pickle", "rb"))
    loaded_model = pickle.load(open(r"api\modelclf.pickle", "rb"))


    sample=corpus

    vectorizer = CountVectorizer()

    bow_transformer = vectorizer.fit(sample)


    messages_bow = bow_transformer.transform(sample)

    tfidf_transformer = TfidfTransformer().fit(messages_bow)

    y_pred=loaded_model.predict(tfidf_transformer.transform(bow_transformer.transform(["Hey there"])))[0]

    return y_pred


