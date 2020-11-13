from behave import given, when, then
import requests
import bs4


@given('a web page url')
def step_imple(context):
    context.url = "https://theanarchistlibrary.org"
@when('we parse a page')
def step_imple(context):
    s = Scraper(context.url)
    context.type = s.parser()
@then('an object of "bs4.BeautifulSoup" is returned')
def step_imple(context):
    assert isinstance(context.type, bs4.BeautifulSoup)


class Scraper:
    def __init__(self, url):
        self.url = url
    def parser(self):
        page = requests.get(self.url)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        return soup
    
