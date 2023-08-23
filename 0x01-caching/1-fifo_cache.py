#!/usr/bin/env python3
"""
FIFO Caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    caching system using FIFO algorithm.
    """
    def __init__(self):
        """
        Initialize the FIFO cache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item in the cache using FIFO algorithm
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.queue.append(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.queue:
                oldest_key = self.queue.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD:", oldest_key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
