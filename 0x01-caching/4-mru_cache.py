#!/usr/bin/python3
"""
Create a class MRUCache that inherits
from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


def copy_dict(items):
    """copies a dictionary"""
    my_dict = {}
    for keys, values in items.items():
        my_dict[keys] = 0
    return my_dict


class MRUCache(BaseCaching):
    """class LRUCache"""
    def __init__(self):
        """Instantiate both parent and child class"""
        super().__init__()
        self.my_dict = copy_dict(self.cache_data)
        self.key = ""

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        cache = self.cache_data
        if len(cache) == self.MAX_ITEMS and key not in cache:
            discard = self.cache_data.pop(self.key)
            self.my_dict.pop(self.key)
            print("DISCARD: {}".format(self.key))
            self.key = key
        if key and item is not None:
            new_element = {key: item}
            self.my_dict.update({key: 0})
            self.cache_data.update(new_element)
        self.save_key = key

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        try:
            self.my_dict[key] += 1
            self.key = key
            return self.cache_data[key]
        except Exception as NotFount:
            return None
