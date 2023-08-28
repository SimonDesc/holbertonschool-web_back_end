#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier """
from typing import List, Set, Dict, Tuple, Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return the function"""

    def multiplication(x):
        """make the multiplication"""
        return x * multiplier

    return multiplication
