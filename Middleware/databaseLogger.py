from pymongo import MongoClient
import blockchainConnector as bc
import datetime
import colours
import sys

try:
    client = MongoClient('mongodb://142.93.131.22:27017/')
    colours.printGreen("Connected to Mongo Client")
    db = client['meterBlockReadings']
except:
    colours.printRed("Could not Connect the mongodb...closing")
    sys.exit()

try:
    address = bc.getNodeAddress()
    collection = db[address]
except:
    colours.printRed("Could not Connect the create collection...closing")
    sys.exit()

def createEntry(power, tokens, isConsuming):
    payload = {"power": power,
            "tokens": tokens,
            "isConsuming": isConsuming,
            "date": datetime.datetime.utcnow()}
    post_id = collection.insert_one(payload).inserted_id
    print(post_id)