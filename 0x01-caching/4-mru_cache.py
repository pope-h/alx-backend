#!/usr/bin/python3
"""
MRUCaching module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    a caching system using MRU algorithm.
    """

    def __init__(self):
        """
        Initialize the MRUCache
        """
        super().__init__()
        self.mru_order = []

    def update_mru_order(self, key):
        """ Update the MRU order """
        if key in self.mru_order:
            self.mru_order.remove(key)
        self.mru_order.append(key)

    def put(self, key, item):
        """
        Add an item in the cache using MRU algorithm
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.mru_order[-1]
            if key not in self.cache_data:
                print("DISCARD:", mru_key)
                self.cache_data.pop(mru_key)
                self.mru_order.pop(-1)

        self.cache_data[key] = item
        self.mru_order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.update_mru_order(key)
        return self.cache_data[key]
