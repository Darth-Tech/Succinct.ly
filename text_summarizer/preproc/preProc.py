# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:53:16 2020

@author: agastya
"""
import re
class CleanText:
    def __init__(self):
        pass
    
    def removeTags(self, soup):
        for script in soup(["script"]):
            script.extract()    

        text = soup.get_text()
        
        return text
    def removeSpaces(self, text):
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        output = ' '.join(chunk for chunk in chunks if chunk)
        
        return output
    def popLinks(self, text):
        regex = r"(?i)\b((?:(http|https|www|ftp|ftps)?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex,text)       
        urls = [x[0] for x in url]
        linkless = re.sub(regex, '', text, flags=re.MULTILINE)
        
        return {'urls':urls, 'linkless':linkless}
    
    def executor(self, text):
        pipes = [self.removeTags, self.removeSpaces, self.popLinks]
        for func in pipes:
            text = func(text)
        return text