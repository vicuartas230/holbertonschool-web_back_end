#!/usr/bin/env python3
""" This script defines a function safely_get_value. """


from typing import Any, Mapping, TypeVar, Union


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[TypeVar('T'),
                                    None] = None) -> Union[Any, TypeVar('T')]:
    """ This function returns a dictionary. """
    if key in dct:
        return dct[key]
    else:
        return default
