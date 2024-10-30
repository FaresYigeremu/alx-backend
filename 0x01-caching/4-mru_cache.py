from base_caching import BaseCaching
""" a class MRUCache that inherits from BaseCaching"""


class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = next(iter(self.cache_data))
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = value
        return value
