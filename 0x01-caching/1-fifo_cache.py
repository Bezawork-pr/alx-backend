#!/usr/bin/python3
"""
Create a class FIFOCache that inherits
from BaseCaching and is a caching system
 use self.cache_data - dictionary from the parent class
 Create two methods"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache"""
    def __init__(self):
        """Instantiate both parent and child class"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print("DISCARD: {}".format(first_key))
            self.cache_data.pop(first_key)

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        try:
            return self.cache_data[key]
        except Exception as NotFount:
            return None
