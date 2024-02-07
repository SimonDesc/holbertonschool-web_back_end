#!/usr/bin/python3
"""
LRUCache Module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class
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
                lru_item = list(self.cache_data.keys())[-1]
                del self.cache_data[lru_item]
                print("DISCARD:", lru_item)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or (key not in self.cache_data):
            return None
        return self.cache_data[key]
