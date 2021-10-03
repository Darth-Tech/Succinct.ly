import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import clustering
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
class Document:
    def __init__(self):
        pass
    def tokenize_and_stem(self, text):
        stemmer = SnowballStemmer("english")
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
        tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        filtered_tokens = []
        # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
        for token in tokens:
            if re.search('[a-zA-Z]', token):
                filtered_tokens.append(token)
        stems = [stemmer.stem(t) for t in filtered_tokens]
        return stems
    def tidfIng(self, text):

        tfidf_vectorizer = TfidfVectorizer(stop_words='english',
                                     use_idf=True, tokenizer=self.tokenize_and_stem, ngram_range=(1,3))
        print(max(text, key=len))
        long = int(len(max(text, key=len))/10)
        text = [tex for tex in text if len(tex)>long]
        tfidf_matrix = tfidf_vectorizer.fit_transform(text)

        return tfidf_matrix, text
