#!/usr/bin/env python3
"""Function that lists all documents in a collection"""


def list_all(mongo_collection):
    """Lists all documents"""
    collection_list = []
    for documents in mongo_collection.find():
        collection_list.append(documents)

    return collection_list

