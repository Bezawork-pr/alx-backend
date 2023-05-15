#!/usr/bin/env python3
"""
This file contains a function that takes two
arguments and returns a tuple
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return start index and end index"""
    return ((page - 1) * page_size, page * page_size)
