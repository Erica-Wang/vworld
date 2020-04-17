import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

client = MongoClient("mongodb+srv://erica:<password>@cluster0-kykqg.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
print (client)

@app.route('/')
def hello():
	return "hi world"

@app.route('/<name>')
def hello_name(name):
	return "Hello {}".format(name)

if __name__ == '__main__':
	app.run()