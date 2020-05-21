# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:15:15 2017
@author: shuai.qian
"""
l = range(1, 100, 2)
h = []
for i in l:
    print(i)
    h.append(i)

print(h[5:])
print('qian shuai is sam.'[:3])

from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance(1234, Iterable))
l = list(range(1, 11))
s = set(l)
print(l)
print(s)
print([x * x for x in range(1, 11, 2)])

print([x * x for x in range(1, 11) if x % 2 == 0])

import os

print([d for d in os.listdir('.')])

d = {'a': 'x', 'b': 'y', 'c': 'z'}

print([k.upper() + '=' + v.upper() for k, v in d.items()])
