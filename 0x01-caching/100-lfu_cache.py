#!/usr/bin/env python3
""" caching system """

from collections import Counter, defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ caching system:

    Args:
        LFUCache ([class]): [basic caching]
    """
    def __init__(self):
        """ initialize of class """
        super().__init__()
        self.frequency = Counter()
        self.item_order = defaultdict(list)

    def put(self, key, item):
        """ Add an item in the cache """
        if not (key is None or item is None):
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                pop = min(self.frequency, key=self.frequency.get)
                self.frequency.pop(pop)
                self.cache_data.pop(pop)
                print(f"DISCARD: {pop}")
            if not (key in self.frequency):
                self.frequency[key] = 0
            else:
                self.frequency[key] += 1

    def get(self, key):
        """ Get an item by key """
        if (key is None) or not (key in self.cache_data):
            return None
        self.frequency[key] += 1
        return self.cache_data.get(key)
