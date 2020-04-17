import constants
from pymongo import MongoClient


client = MongoClient(constants.MONGO_URL)
db = client.world
print (client)

#movement: 1 step = 50pxs
#stepTurn: how many steps before turn

stepTurn = [4,2,6,7,2,4,5,7,1]


