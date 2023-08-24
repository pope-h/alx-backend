#!/usr/bin/python3
"""
LRUCaching module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    a caching system using LRU algorithm.
    """

    def __init__(self):
        """
        Initialize the LRUCache
        """
        super().__init__()  # Call the parent class's __init__() method
        self.lru_order = []

    def update_lru_order(self, key):
        """ Update the LRU order """
        if key in self.lru_order:
            self.lru_order.remove(key)
        self.lru_order.append(key)

    def put(self, key, item):
        """
        Add an item in the cache using LRU algorithm
        """
        if key is None and item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.lru_order[0]
            if key not in self.cache_data:
                print("DISCARD:", lru_key)
            self.cache_data.pop(lru_key)
            self.lru_order.pop(0)

        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.update_lru_order(key)
        return self.cache_data[key]
