#!/usr/bin/env python3
"""8-main"""


def list_all(mongo_collection):
    """
    lists all documents in a MongoDB collection.

    args:
        mongo_collection: The pymongo collection object to query.

    returns:
        A list of documents (dictionaries), or an empty list if none found.
    """

    return list(mongo_collection.find())
