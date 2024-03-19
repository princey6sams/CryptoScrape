from pymongo import MongoClient
import os

uri = os.environ.get('MONGO_URI')
client = MongoClient(uri)

db = client["Backend"]

def connectToMongo():
    print("Connected to MongoDB")
    return db

def closeConnection():
    print("Connection to MongoDB closed")
    client.close()