#!/usr/bin/env python3
"""A function to return the start and
end index for a particular pagination parameters """


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
