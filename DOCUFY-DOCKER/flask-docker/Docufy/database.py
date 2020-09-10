import pymongo
from pymongo import MongoClient
class Database:
    # client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

    client = pymongo.MongoClient("mongodb+srv://shantanu:shantanupass@cluster0-e8mqp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test


    @staticmethod
    def insert(collection, data):
        Database.db[collection].insert(data)

    @staticmethod
    def find_one(collection, query):
        return Database.db[collection].find_one(query)

    @staticmethod
    def find(collection, query):
        return Database.db[collection].find(query)

    @staticmethod
    def update_one(collection, query, newval):
        return Database.db[collection].update_one(query, newval)