#!/usr/bin/env python3
""" This script defines a function element_length. """


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ This function returns a list. """
    return [(i, len(i)) for i in lst]
