from scraper import Scraper
from core import Summary
from tfIdf import Document
from topic_headlines import Topics
import clustering
import pandas as pd
class Executor:
    def __init__(self, url, model):
        self.scrape = Scraper(url)
        self.summary = Summary(model=model)
    def topicHandling(self, doc):
        topic = Topics()
        topics = topic.LDA(doc)
        return topics[1]
    def execute(self):
        data = self.scrape.scraper()
        data['linkless'] = self.summary.summarize(data['linkless'])
        tfid = Document()
        matrix, text = tfid.tidfIng(data['linkless'])
        c = clustering.Cluster()
        df = c.bestK(matrix, text)
        new = pd.DataFrame()
        for cluster in df['results'].unique():
            doc = df[df['results']==cluster]['text'].tolist()
            temp = df[df['results']==cluster]
            topics = self.topicHandling(doc)
            print(topics)
            temp['topics'] = topics
            new = new.append(temp)
        return new, data['urls']
