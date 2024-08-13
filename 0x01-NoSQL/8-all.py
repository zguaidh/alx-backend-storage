#!/usr/bin/env python3
'''Lists all documents in a collection'''


from pymongo import MongoClient


def list_all(mongo_collection):
    '''Returns all documents in a collection'''
    doc = []
    doc.append(mango_collection.find())
    return doc
