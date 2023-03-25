import pickle
import string
from sentence_transformers import SentenceTransformer, util
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
def predict(content):
    corpus = pickle.load(open(r"api\textcorpus.pickle", "rb"))
    loaded_model = pickle.load(open(r"api\modelclf.pickle", "rb"))


    sample=corpus

    vectorizer = CountVectorizer()

    bow_transformer = vectorizer.fit(sample)


    messages_bow = bow_transformer.transform(sample)

    tfidf_transformer = TfidfTransformer().fit(messages_bow)

    y_pred=loaded_model.predict(tfidf_transformer.transform(bow_transformer.transform([content])))[0]

    return y_pred

def bert(content):
    model = SentenceTransformer('all-mpnet-base-v2')

    test_emb = model.encode(content)
    data_emb=pickle.load(open(r"api\trainembedding.pickle",'rb'))

    cos = numpy.dot(data_emb, test_emb) / (numpy.sqrt(numpy.dot(data_emb,data_emb)) * numpy.sqrt(numpy.dot(test_emb,test_emb)))
    return cos
