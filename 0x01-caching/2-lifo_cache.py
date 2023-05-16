#!/usr/bin/python3
"""Create a class LIFOCache that inherits
from BaseCaching and is a caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache"""
    def __init__(self):
        """Instantiate both parent and child class"""
        super().__init__()
        self.save_key = ""

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if len(self.cache_data) == self.MAX_ITEMS:
            discard = self.cache_data.pop(self.save_key)
            print("DISCARD: {}".format(self.save_key))
        if key and item is not None:
            new_element = { key: item }
            self.cache_data.update(new_element)
            #self.cache_data[key] = item
        self.save_key = key

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        try:
            return self.cache_data[key]
        except Exception as NotFount:
            return None
