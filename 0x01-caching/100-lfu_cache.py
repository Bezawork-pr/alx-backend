#!/usr/bin/python3
"""
Create a class LFUCache that inherits from
BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


def copy_dict(items):
    """copies a dictionary"""
    my_dict = {}
    for keys, values in items.items():
        my_dict[keys] = 0
    return my_dict


class LFUCache(BaseCaching):
    """class LFUCache"""
    def __init__(self):
        """Instantiate both parent and child class"""
        super().__init__()
        self.my_dict = copy_dict(self.cache_data)

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        cache = self.cache_data
        if item is not None and key in cache:
            self.my_dict[key] = self.my_dict[key] + 1
            new_element = {key: item}
            self.cache_data.update(new_element)
        if len(cache) == self.MAX_ITEMS and key not in cache:
            least_value = list(self.my_dict.items())[0][1]
            least_assessed_key = next(iter(self.cache_data))
            for keys, values in self.my_dict.items():
                if least_value > values:
                    least_value = values
                    least_assessed_key = keys
            discard = self.cache_data.pop(least_assessed_key)
            self.my_dict.pop(least_assessed_key)
            print("DISCARD: {}".format(least_assessed_key))
        if key and item is not None and key not in cache:
            new_element = {key: item}
            self.my_dict.update({key: 0})
            self.cache_data.update(new_element)

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        try:
            if key == "C":
                print(self.my_dict)
            self.my_dict[key] = self.my_dict[key] + 1
            return self.cache_data[key]
        except Exception as NotFount:
            return None
