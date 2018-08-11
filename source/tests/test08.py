# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:37:37 2017
@author: shuai.qian
"""

# map reduce
from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))


def fn(x, y):
    return x * 10 + y


g = reduce(fn, [1, 2, 3, 4])
print(g)
print('===============><===============')


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(fn, map(char2num, '2312')))

print(f.__name__)
