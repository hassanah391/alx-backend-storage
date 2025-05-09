#!/usr/bin/env python3
"""11-schools_by_topic.py"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools that have the given topic in their 'topics' field.
    
    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object.
        topic (str): The topic to search for within the 'topics' field.
        
    Returns:
        list: A list of schools (documents) where the 'topics' field contains the given topic.
    """
    return list(mongo_collection.find({"topics": topic}))
