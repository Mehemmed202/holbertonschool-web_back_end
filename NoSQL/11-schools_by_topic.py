#!/usr/bin/env python3
"""
this module defines a function to find documents based on a list item.
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of schools having a specific topic.

    args:
        mongo_collection: the pymongo collection object.
        topic (str): the topic to search for.

    returns:
        list: A list of dictionaries (documents) matching the topic.
    """

    search = {"topic": topic}
    return mongo_collection.find(search)
