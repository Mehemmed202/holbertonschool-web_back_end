#!/usr/bin/env python3
"""11-schools_by_topic.py11-schools_by_topic.py"""


def schools_by_topic(mongo_collection, topic):
    """def schools_by_topic(mongo_collection, topic):def schools_by_topic(mongo_collection, topic):def schools_by_topic(mongo_collection, topic):"""

    search = {"topic": topic}
    return mongo_collection.find(search)
