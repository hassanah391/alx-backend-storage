#!/usr/bin/env python3
""" Inserts a new document into a MongoDB collection using **kwargs """


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into mongo_collection using keyword arguments

    Args:
        mongo_collection: The pymongo collection object
        **kwargs: Fields for the new document

    Returns:
        The _id of the newly inserted document
    """
    document = dict(kwargs)  # converts kwargs to a dictionary
    result = mongo_collection.insert_one(document)
    return result.inserted_id
