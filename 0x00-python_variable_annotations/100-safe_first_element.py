#!/usr/bin/env python3
""" This script defines a function safe_first_element. """


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ This function return the first element of a list or none if empty. """
    if lst:
        return lst[0]
    else:
        return None
