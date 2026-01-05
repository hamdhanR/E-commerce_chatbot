# app/database.py
import pymongo

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "e-commerce"

mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]
