#!/usr/bin/env python3
"""Function that changes all topics of a school document
based on the name"""


def schools_by_topic(mongo_collection, topic):
    """return the list of a specific topic"""
    collection_list = []
    for documents in mongo_collection.find({"topics": topic}):
        collection_list.append(documents)

    return collection_list
