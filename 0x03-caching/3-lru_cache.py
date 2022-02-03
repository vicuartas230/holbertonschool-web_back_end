#!/usr/bin/env python3
""" This script defines a class LRUCache. """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ This class defines put and get methods. """
    def __init__(self):
        """ This method intializes a class LRUCache. """
        super().__init__()

    def put(self, key, item):
        """ This method assign an item to dictionary cache_data. """
        if key and item:
            if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
                if key in list(self.cache_data.keys()):
                    del self.cache_data[key]
                    self.cache_data.update({key: item})
                    return
                else:
                    print("DISCARD: {}\
".format(list(self.cache_data.keys())[0]))
                    self.cache_data.pop(list(self.cache_data.keys())[0])
            self.cache_data[key] = item

    def get(self, key):
        """ This method gets an item by key in dictionary cache_data. """
        if not key or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
