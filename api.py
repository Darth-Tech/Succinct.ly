# -*- coding: utf-8 -*-
"""
Created on Thur Sep 24 17:54:28 2020
@author: polo
"""
from flask import Flask
from flask_restx import Api, Resource
from flask import request
from scraper import Scraper

flask_app = Flask(__name__)
#app = Flask(__name__)
app = Api(app=flask_app)

name_space = app.namespace('Text Summarizer', description='Enter the url of the page and the text will be summarized yay')

@name_space.route("")
@name_space.doc(params={'url':{'URL enter':'Please enter the URL','in':'query','type':'string'}})
class MainClass(Resource):
    def get(self):
        scrap = Scraper(str(request.args.get('url')))
        res = scrap.scraper()
        return {
            "urls": res['urls'],
            "linkless": res['linkless']
        }

    

if __name__ == '__main__':
    flask_app.run(debug=False, host='0.0.0.0')
