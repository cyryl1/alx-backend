#!/usr/bin/env python3

"""Basic Dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Dictionary"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """
        Put item into cache with given key.
        Args:
            key (str): The key for the item
            item (any): The item to cache
        """
        if key is None or item is None:
            return None

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

        value = self.cache_data.get(key)
        return value
