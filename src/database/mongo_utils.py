from pymongo import MongoClient
import os

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["twitter_trends"]
    collection = db["trends"]
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")

def insert_record(record):
    collection.insert_one(record)

def fetch_latest_record():
    return collection.find_one(sort=[("_id", -1)])