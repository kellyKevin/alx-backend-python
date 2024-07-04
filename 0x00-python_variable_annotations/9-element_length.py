#!/usr/bin/env python3
""" Module documentation """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Func doc"""
    return [(i, len(i)) for i in lst]
