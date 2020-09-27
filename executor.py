from scraper import Scraper
from core import Summary
class Executor:
    def __init__(self, url):
        self.scrape = Scraper(url)
        self.summary = self.Summary()
    def execute(self):
        data = self.scrape.scraper()
        text = self.summary.summarize(data['linkless'])
        return text