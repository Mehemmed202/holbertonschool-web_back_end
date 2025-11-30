#!/usr/bin/env python3
"""a"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name.

    args:
        mongo_collection: the pymongo collection object.
        name (str): the name of the school to update.
        topics (list of str): the list of topics approached in the school.
    """

    mongo_collection.update_many(
    {"name": name},
    {$set: {"topics": topics}}
    {multi: true}
            )


