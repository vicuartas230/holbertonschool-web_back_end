#!/usr/bin/env python3
""" This script defines a class BasicCache. """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ This class defines put and get methods. """
    def __init__(self):
        """ This method initializes de BasicCache class. """
        super().__init__()

    def put(self, key, item):
        """ This method assigns a item to cache_data dictionary. """
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """ This method gets the value of a key in cache_data dictionary. """
        if not key or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
