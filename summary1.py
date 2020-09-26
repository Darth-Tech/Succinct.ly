from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
nltk.download('punkt')

LANGUAGE = "english"

def summary(url):
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    SENTENCES_COUNT = 0
    for sent in parser.document.sentences:
        SENTENCES_COUNT += 1
    SENTENCES_COUNT /= 3
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    res = []
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        res.append(str(sentence))
    return " ".join(res)