#!/usr/bin/python3
"""
Inheret from BaseCaching
Use self.cache_data from dictionary
Create method put create get
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache"""
    def __init__(self):
        """Instanciate"""
        super().__init__()

    def put(self, key, item):
        """Assign to self.cache_data"""
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return value linked to the key"""
        try:
            return self.cache_data[key]
        except Exception as NotFound:
            return None
