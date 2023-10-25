#!/usr/bin/env python3
""" caching module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.keys) == BaseCaching.MAX_ITEMS:
            discarded = self.keys.pop()
            del self.cache_data[discarded]
            print(f"DISCARD: {discarded}")
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
