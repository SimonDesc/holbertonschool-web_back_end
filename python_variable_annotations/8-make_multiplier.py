#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function"""
from typing import List, Set, Dict, Tuple, Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return the function"""

    def multiplication(x):
        """make the multiplication"""
        return x * multiplier

    return multiplication
