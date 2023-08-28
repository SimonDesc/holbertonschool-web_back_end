#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function"""
from typing import List, Set, Dict, Tuple, Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return the function"""
    return multiplication


def multiplication(multiplier):
    """make the multiplication"""
    return multiplier * multiplier
