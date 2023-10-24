#!/usr/bin/env python3
""" cache inherti from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        if (key or item) is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if(key is None):
            return None
        else:
            return self.cache_data.get(key, None)
