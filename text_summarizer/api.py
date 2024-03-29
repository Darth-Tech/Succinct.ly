# -*- coding: utf-8 -*-
"""
Created on Thur Sep 24 17:54:28 2020
@author: polo
"""
from summarizer import Summarizer
from flask import Flask
from flask_restx import Api, Resource
from flask import request
from executor import Executor
model = Summarizer()
flask_app = Flask(__name__)
#app = Flask(__name__)
app = Api(app=flask_app)
name_space = app.namespace('textSummarizer', description='Enter the url of the page and the text will be summarized yay')

@name_space.route("")
@name_space.doc(params={'url':{'URL enter':'Please enter the URL','in':'query','type':'string'}})
class MainClass(Resource):
    def get(self):
        print("Testing...")
        
        print("Hi")
        test = model("QWERTYUIOPQWERTYUIO DFGH DFGHJ YUIO RTGHJ") 
        executor = Executor(str(request.args.get('url')), model)
        res = executor.execute()
        return {
            "urls": str(res['urls']),
            "linkless": str(res['linkless'])
        }

    

if __name__ == '__main__':
    
    flask_app.run(debug=True, host='0.0.0.0', use_reloader=False)
      
