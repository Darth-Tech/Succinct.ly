from scraper import Scraper
from core import Summary
class Executor:
    def __init__(self, url, model):
        self.scrape = Scraper(url)
        self.summary = Summary(model)
    def execute(self):
        data = self.scrape.scraper()
        data['linkless'] = self.summary.summarize(data['linkless'])
        return data
