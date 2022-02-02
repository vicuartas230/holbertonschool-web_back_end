#!/usr/bin/env python3
""" This script defines a function sum_list. """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ This function takes a list input_list
        of floats as argument and returns their sum as a float. """
    acum = 0
    for n in input_list:
        acum += n
    return acum
