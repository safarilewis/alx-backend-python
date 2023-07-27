#!/usr/bin/env python3
'''More involved type annotations'''
from typing import TypeVar, Any, Mapping, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    '''Gets value from a list using key
    '''
    if key in dct:
        return dct[key]
    else:
        return default
