#!/usr/bin/python3
"""
LIFOCache Module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class

    Implements a cache storage mechanism that follows the Last In,
    First Out (LIFO)
    principle. When the cache exceeds its maximum size, the most
    recently added item
    before the new addition is removed.
    """

    def __init__(self):
        return super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_item = list(self.cache_data.keys())[-1]
                del self.cache_data[last_item]
                print("DISCARD:", last_item)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or (key not in self.cache_data):
            return None
        return self.cache_data[key]
