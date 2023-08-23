#!/usr/bin/python3
"""
LIFOCaching module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    a caching system using LIFO algorithm.
    """
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item in the cache using LIFO algorithm
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.stack.remove(key)
                else:
                    del self.cache_data[self.stack[self.MAX_ITEMS - 1]]
                    item_discarded = self.stack.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
