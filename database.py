from pymongo import MongoClient
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "sample_mflix"  # Use your specific database name
COLLECTION_NAME = "movies"  # Use your specific collection name

def get_mongo_client():
    return MongoClient(MONGO_URI)

def get_movies_collection():
    client = get_mongo_client()
    db = client[DB_NAME]
    return db[COLLECTION_NAME]

def search_movies(query):
    collection = get_movies_collection()
    # Perform case-insensitive search for movie titles based on the query
    results = collection.find({"title": {"$regex": query, "$options": "i"}}).limit(5)
    return list(results)

def get_interactions_collection():
    client = get_mongo_client()
    db = client["chatbot_interactions"]  # New database to store interactions
    return db["interactions"]  # Interactions collection


def store_interaction(user_input, bot_response, movies_found):
    collection = get_interactions_collection()
    interaction_data = {
        "user_input": user_input,
        "bot_response": bot_response,
        "movies_found": movies_found,
        "timestamp": datetime.datetime.now()
    }
    collection.insert_one(interaction_data)

