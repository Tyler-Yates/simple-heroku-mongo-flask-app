import datetime
import os

from bson import ObjectId
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.results import InsertOneResult

# Set the documents to expire after a set amount of time
TTL_SECONDS = 6 * 60 * 60


class ApplicationDao:
    def __init__(self):
        username = os.environ.get("MONGO_USER")
        password = os.environ.get("MONGO_PASSWORD")
        host = os.environ.get("MONGO_HOST")
        self.client = MongoClient(
            f"mongodb+srv://{username}:{password}@{host}/test?retryWrites=true&w=majority"
        )

        self.database: Database = self.client.test

        self.test_collection: Collection = self.database.test_collection
        # Set a TTL on the test collection
        self.test_collection.create_index('createdAt', expireAfterSeconds=TTL_SECONDS)

        print(f"Database collections: {self.database.list_collection_names()}")

    def insert_document(self, text: str) -> InsertOneResult:
        return self.test_collection.insert_one({
            "createdAt": datetime.datetime.utcnow(),
            "text": text
        })

    def get_documents(self):
        return self.test_collection.find()

    def get_document(self, document_id) -> dict:
        return self.test_collection.find_one({
            "_id": ObjectId(document_id)
        })

    def delete_document(self, document_id):
        return self.test_collection.delete_one({
            "_id": ObjectId(document_id)
        })

    def delete_documents(self):
        return self.test_collection.delete_many({})
