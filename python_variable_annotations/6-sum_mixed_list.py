#!/usr/bin/env python3
"""Write a type-annotated function sum_list which takes a list"""
from typing import List, Set, Dict, Tuple, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the sum of a list"""
    return sum(mxd_lst)
