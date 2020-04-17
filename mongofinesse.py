import os
from pymongo import MongoClient
import constants
from random import randint

client = MongoClient(constants.MONGO_URL)
db = client.world
print (client)

collection = db.people
people = []
for person in collection.find():
	p = {
		"id":person['id'],
		"x":person['x'],
		"y":person['y']
	}
	people.append(p)
print(people)