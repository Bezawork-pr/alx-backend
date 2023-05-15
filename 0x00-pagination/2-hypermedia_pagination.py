#!/usr/bin/env python3
"""
This file contains a function and a class
"""
from typing import Tuple
import csv
import math
from typing import List, Dict


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
        Get page from start to end calculated by index_range function
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        [start, end] = index_range(page, page_size)
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        returns a dictionary containing the following key-value pairs
        """
        data = self.get_page(page, page_size)
        total_pages = int(len(self.__dataset) / page_size)
        next_page = page + 1 if page + 1 < total_pages else None
        prev_page = page - 1 if page - 1 > 0 else None
        return {"page_size": len(data),
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return start index and end index"""
    return ((page - 1) * page_size, page * page_size)
