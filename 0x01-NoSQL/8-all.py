#!/usr/bin/env python3
'''Lists all documents in a collection'''


from pymongo import MongoClient


def list_all(mongo_collection):
    '''Returns all documents in a collection'''
    if mongo_collection.find():
        return mongo_collection.find()
    else:
        return []
