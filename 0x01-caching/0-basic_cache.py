#!/usr/bin/env python3
""" cache inherti from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """  Defines a class for caching information
         in key-value pair """
    def __init__(self):
        """ Initialize the class using the parent class """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """ Store a key-value pair """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ If key is None or doesn't exist, return None """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
