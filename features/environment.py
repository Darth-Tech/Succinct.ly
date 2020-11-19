# -- FILE: features/environment.py
# HINT: Reusing some code parts from above. 
import bs4
import requests

def before_feature(context, feature):
    if "clean" in feature.tags:
        page = requests.get(self.url)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        