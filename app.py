import os
from flask import Flask


app = Flask(__name__)
environment_configuration = os.environ['APP_SETTINGS']
app.config.from_object(environment_configuration)
# app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    #return "Hello World!"
    return os.environ['APP_SETTINGS']


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
