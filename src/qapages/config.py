import os
from functools import lru_cache

from pymongo import MongoClient
from pymongo.database import Database as MongoDatabase


@lru_cache
def get_mongo_db() -> MongoDatabase:
    _client = MongoClient(
        host=os.getenv("MONGO_HOST"),
        username=os.getenv("MONGO_USERNAME"),
        password=os.getenv("MONGO_PASSWORD"),
    )
    return _client["qapages"]
