#!/usr/bin/python3
"""
Create a class LRUCache that inherits
from BaseCaching and is a caching system"""
BaseCaching = __import__('base_caching').BaseCaching


def copy_dict(items):
    my_dict = {}
    for keys, values in items.items():
        my_dict[keys] = 0
    return my_dict


class LRUCache(BaseCaching):
    """class LRUCache"""
    def __init__(self):
        """Instantiate both parent and child class"""
        super().__init__()
        self.save_key = ""
        self.my_dict = copy_dict(self.cache_data)

    def put(self, key, item):

        """assign to the dictionary self.cache_data"""
        print(self.my_dict)
        if len(self.cache_data) == self.MAX_ITEMS
        and key not in self.cache_data:
            self.my_dict.pop(self.save_key)
            least_assessed = 0
            least_assessed_key = next(iter(self.cache_data))
            for keys, values in self.my_dict.items():
                if least_assessed > values:
                    least_assessed = values
                    least_assessed_key = keys
            discard = self.cache_data.pop(least_assessed_key)
            print("DISCARD: {}".format(least_assessed_key))
        if key and item is not None:
            new_element = {key: item}
            self.my_dict.update({key: 0})
            self.cache_data.update(new_element)
        self.save_key = key

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        try:
            self.my_dict[key] += 1
            return self.cache_data[key]
        except Exception as NotFount:
            return None
