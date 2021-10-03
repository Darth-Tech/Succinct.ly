import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import gensim
from gensim import corpora
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
#doc1 = "The Chrysler Building, the famous art deco New York skyscraper, will be sold for a small fraction of its previous sales price."
#doc2 = "The deal, first reported by The Real Deal, was for $150 million, according to a source familiar with the deal."
#doc3 = "While the building is an iconic landmark in the New York skyline, it is competing against newer office towers with large floor-to-ceiling windows and all the modern amenities."
#doc4 = "It is famous for its triangle-shaped, vaulted windows worked into the stylized crown, along with its distinctive eagle gargoyles near the top."
#doc5 = "The Chrysler Building was the headquarters of the American automaker until 1953, but it was named for and owned by Chrysler chief Walter Chrysler, not the company itself."#

#doc_complete = [doc1, doc2, doc3, doc4, doc5]
#stop = set(stopwords.words('english'))
#exclude = set(string.punctuation)
#lemma = WordNetLemmatizer()
#def clean(doc):
#    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
#    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
#    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
#    return normalized

#doc_clean = [clean(doc).split() for doc in doc_complete]
#dictionary = corpora.Dictionary(doc_clean)
#doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

#Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
#ldamodel = Lda(doc_term_matrix, num_topics=1, id2word = dictionary, passes=100)
#print(ldamodel.print_topics(num_topics=1, num_words=3))
class Topics:
    def clean(self, doc):
        stop = set(stopwords.words('english'))
        exclude = set(string.punctuation)
        lemma = WordNetLemmatizer()
        stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
        punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
        normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
        return normalized
    def preprocessing(self, doc_complete):
        doc_clean = [self.clean(doc).split() for doc in doc_complete]
        dictionary = corpora.Dictionary(doc_clean)
        doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
        return doc_term_matrix, dictionary
    def LDA(self, doc):
        Lda = gensim.models.ldamodel.LdaModel
        doc_term_matrix, dictionary = self.preprocessing(doc)
        # Running and Trainign LDA model on the document term matrix.
        ldamodel = Lda(doc_term_matrix, num_topics=1, id2word = dictionary, passes=100)
        print("topics: ", ldamodel.show_topics(num_topics=1, num_words=3)[0])
        data = ldamodel.show_topics(num_topics=1, num_words=3)[0]
        return data
