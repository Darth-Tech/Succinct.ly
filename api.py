from flask import Flask
from flask_restplus import Api, Resource
from flask import request
from summary1 import summary

flask_app = Flask(__name__)
#app = Flask(__name__)
app = Api(app=flask_app)

name_space = app.namespace('Text Summarizer', description='enter the url of the page and the text will be summarized yay')

@name_space.route("")
@name_space.doc(params={'url':{'URL enter':'Please enter the URL','in':'query','type':'string'}})
class MainClass(Resource):
    def get(self):
        res = summary(str(request.args.get('url')))
        return {
            "summary": str(res)
        }

    

if __name__ == '__main__':
    flask_app.run()