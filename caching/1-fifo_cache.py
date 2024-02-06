#!/usr/bin/python3
"""
FIFOCache Module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching class implementing the FIFO (First In, First Out)
    mechanism. It inherits from BaseCaching and allows storing items with a
    maximum limit. When the limit is exceeded upon adding a new item, the
    first added (oldest) item is discarded.

    Methods:
    __init__(self): Initializes the cache with the BaseCaching constructor.

    put(self, key, item): Adds an item to the cache.
        - If key or item is None, does nothing.
        - If adding causes exceeding BaseCaching.MAX_ITEMS, discards the
          first added item.

    get(self, key): Retrieves an item by key.
        - Returns None if key is None or not in the cache.
        - Otherwise, returns the item associated with the key.
    """

    def __init__(self):
        return super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_key)
                print("DISCARD:", first_key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or (key not in self.cache_data):
            return None
        return self.cache_data[key]
