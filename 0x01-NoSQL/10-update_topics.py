#!/usr/bin/env python3
"""
Module to update the topics of a school in a MongoDB collection.

This module defines a function `update_topics` that updates the topics
of a specific school based on its name in a MongoDB collection. The topics
are replaced with a new list provided to the function.

Usage:
    Call the `update_topics` function with a MongoDB collection, a school name,
    and a list of new topics to update the school’s topics field.

Example:
    update_topics(collection, "ALX", ["Sys admin", "AI", "Algorithm"])
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school in the MongoDB collection based on its name.

    This function finds all documents in the collection
    where the 'name' field matches
    the provided 'name' and updates the 'topics' field with
    the new list of topics.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection to update.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set in the 'topics' field.

    Returns:
        None: This function does not return anything.
        It directly updates the documents.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
