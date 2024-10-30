#!/usr/bin/env python3
from basic_caching import BaseCaching
from collections import OrderedDict
"""FIFO Cache"""


class FIFOCache(BaseCaching):
    """A class representation for FIFO Caching"""

    def __init__(self):
        """Initialize cache"""
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

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

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
