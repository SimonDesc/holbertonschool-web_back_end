#!/usr/bin/env python3
"""Write a type-annotated function sum_list which takes a list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return the sum of a list"""
    return sum(input_list)
