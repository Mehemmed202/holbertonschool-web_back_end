#!/usr/bin/env python3
"""a"""


def update_topics(mongo_collection, name, topics):
    """aaaaaaaa


    aaaaa"""

    mongo_collection.update_many(
    {"name": name},
    {$set: {"topics": topics}}
    {multi: true}
            )


