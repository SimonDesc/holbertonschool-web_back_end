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
        super().__init__()
        self.order_used_item = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            if key in self.cache_data:
                self.order_used_item.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_item = self.order_used_item.pop(0)
                del self.cache_data[lru_item]
                print("DISCARD:", lru_item)
            self.cache_data[key] = item
            self.order_used_item.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or (key not in self.cache_data):
            return None
        if key in self.order_used_item:
            self.order_used_item.remove(key)
        self.order_used_item.append(key)
        return self.cache_data[key]
