#!/usr/bin/env python3
'''Lists all documents in a collection'''


from pymongo import MongoClient


def list_all(mongo_collection):
    '''Returns all documents in a collection'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    doc = []
    for doc in client.my_db.mango_collection.find()
        doc.append(client.my_db.mango_collection.find())
    return doc
