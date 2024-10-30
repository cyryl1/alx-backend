#!/usr/bin/env python3
from basic_caching import BaseCaching
from collections import OrderedDict
"""FIFO Cache"""


class LIFOCache(BaseCaching):
    """A class representation for FIFO Caching"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Put item into cache with given key.
        Args:
            key (str): The key for the item
            item (any): The item to cache
        """
        if key is None or item is None:
            return None

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Get item from cache with given key.
        Args:
            key (str): The key for the item
        Returns:
        any: The item from cache if found, otherwise None
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
