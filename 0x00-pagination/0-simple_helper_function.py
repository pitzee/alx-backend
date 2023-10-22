#!/usr/bin/env python3
""" Contains definition of index
     _range helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Takes 2 integer arguments and returns a tuple
    of sizev  ontaining the start and end index """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
