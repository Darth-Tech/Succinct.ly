# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:18:08 2020

@author: agastya
"""
import requests
import bs4
import re
from preproc.preProc import CleanText
class Scraper:
    def __init__(self, url):
        self.url = url
        self.clean = CleanText()
    def parser(self):
        page = requests.get(self.url)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')

        return soup
    def findTextAll(self):
        soup = self.parser()
        output = self.clean.executor(soup)

        return output
    def scraper(self):
        output = self.findTextAll()
        return output

