#!/usr/bin/env python3
"""return values with the appropriate types"""
from typing import List, Set, Dict, Tuple, Union, Callable, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Let's duck type an iterable object"""
    return [(i, len(i)) for i in lst]
