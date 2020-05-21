# -*- coding: utf-8 -*-
"""
Created on 11/27/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])

pos = (n for n in mylist if n > 0)
print(type(pos))

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return x
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

from itertools import compress

counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
print(more5)
addr = ['5800 E ', '4801 D', '9090 F', '8989 G', '9999 H']
print(list(compress(addr, more5)))
