from behave import given, when, then

@given('a text with hyperlinks')
def step_imple(context):
    context.data = context.text
    context.urls = ['www.google.com', 'http://testsite.org', 'www.testnet.net', 'https://theanarchistlibrary.org/']
@when('we preprocess this ')
def step_imple(context):
    clean = CleanText()
    context.results = clean.popLinks(context.data)
@then('the result splits the text and the hyperlinks to summarise')
def step_imple(context):
    assert set(context.urls)==set(context.results['urls'])






class CleanText:
    def __init__(self):
        pass
    def popLinks(self, text):
        regex = r"(?i)\b((?:(http|https|www|ftp|ftps)?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,text)       
        urls = [x[0] for x in url]
        linkless = re.sub(regex, '', text, flags=re.MULTILINE)
        
        return {'urls':urls, 'linkless':linkless}
