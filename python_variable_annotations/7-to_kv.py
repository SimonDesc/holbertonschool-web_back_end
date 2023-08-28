#!/usr/bin/env python3
"""Write a type-annotated function sum_list which takes a list"""
from typing import List, Set, Dict, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return the sum of a list"""
    return (k, v * v)
