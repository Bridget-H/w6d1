from flask import Flask 

app = Flask(__name__)

#class Config:
#    FLASK_APP = 'run'
#    FLASK_ENV = 'developement'

#app.config.from_object(Config)

@app.route('/')
def index():
    return '<h1>Hello Wor </h1>'

@app.route('/test')
def test():
    return'This is a test'