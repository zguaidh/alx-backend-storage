#!/usr/bin/env python3
'''Inserts a new documents in a collection'''


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    '''Iserts a new document in a collection'''
    result = mongo_collection.insert_one( kwargs )
    return result.inserted_id
