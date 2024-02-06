#!/usr/bin/python3
from base_caching import BaseCaching
""" BasicCache Module
"""


class BasicCache(BaseCaching):
    """
    The BasicCache class is a subclass of
    BaseCaching that implements a simple caching mechanism using a
    dictionary to store key-value pairs.
    """

    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key is None or (key not in self.cache_data):
            return None
        return self.cache_data[key]
