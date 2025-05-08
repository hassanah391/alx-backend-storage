#!/usr/bin/env python3
""" Function that lists all documents in a MongoDB collection """
from pymongo import MongoClient


def list_all(mongo_collection):
    """Lists all documents in the given MongoDB collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        A list of documents, or an empty list if none found.
    """
    return list(mongo_collection.find())

