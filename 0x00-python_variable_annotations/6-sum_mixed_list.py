#!/usr/bin/env python3
""" This script defines a function sum_mixed_list. """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ This function takes a list mxd_lst of integers and
        floats and returns their sum as a float. """
    acum = 0
    for n in mxd_lst:
        acum += n
    return acum
