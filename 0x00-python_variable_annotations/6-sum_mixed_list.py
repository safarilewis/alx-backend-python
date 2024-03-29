#!/usr/bin/env python3
'''Mixed list annotation
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the sum of a list of ints & floats
    '''
    tot = 0
    for x in mxd_lst:
        tot = tot + x
    return tot
