import os
from pymongo import MongoClient
import constants
from random import randint

client = MongoClient(constants.MONGO_URL)
db = client.world
print (client)
print(randint(1,5))
db.people.update_many({}, [
        {"$set": {"stepsTaken": { $subtract: [ "$stepsBeforeTurn", 1 ] }}}
    ])