#!/usr/bin/env python3

'''Duck typing - first element of a sequence
'''
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns the first element of a Sequence
    '''
    if lst:
        return lst[0]
    else:
        return None
