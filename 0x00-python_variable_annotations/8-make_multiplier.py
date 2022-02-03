#!/usr/bin/env python3
""" This script defines a function make_multiplier. """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This function takes a float multiplier as argument and returns
        a function that multiplies a float by multiplier. """
    def inner(mul: float) -> float:
        """ This function multiplies a float by multiplier. """
        return mul * multiplier
    return inner
