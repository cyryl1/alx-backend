#!/usr/bin/env python3
import csv
import math
from typing import List, Dict

"""A function to return the start and end
index for a particular pagination parameters """


def index_range(page: int, page_size: int):
    """
    Given a page number and a page size,
    return the start and end index for pagination.
    Args:
        page (int): The page number (1-based)
        page_size (int): The number of items per page

    Returns:
        tuple of size two containing a start index and an end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of data from the dataset.
        Args:
            page (int): The page number (1-based)
            page_size (int): The number of items per page

        Returns:
            List of items on the page.
            If the page number is out of range, returns an empty list.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        assert page <= len(dataset)
        if end_index > len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Pagination with hypermedia metadata

        Args:
        page (int): The page number (1-based)
        page_size (int): The number of items per page

        Returns:
        Dictionary containing items and pagination metadata
        """
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        page_items = self.get_page(page, page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": page_items,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_page": total_pages
        }
