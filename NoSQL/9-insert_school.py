#!/usr/bin/env python3
"""9-insert_school.py"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs.

    args:
        mongo_collection: the pymongo collection object.
        **kwargs: arbitrary keyword arguments to be inserted as the document.

    returns:
        the _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
