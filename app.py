import os
from flask import Flask
from pymongo import MongoClient
import constants
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

cors = CORS(app)

client = MongoClient(constants.MONGO_URL)
db = client.world
print (client)

@app.route('/')
def hello():
	return "hi world"

@app.route('/locations')
def getLocations():
	collection = db.people
	people = []
	for person in collection.find():
		p = {
			"id":person['id'],
			"x":person['x'],
			"y":person['y']
		}
		people.append(p)
	return jsonify(people)

if __name__ == '__main__':
	app.run()