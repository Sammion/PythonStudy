# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:17:22 2017

@author: shuai.qian
"""
from collections import namedtuple, deque, defaultdict


Point = namedtuple('Point',['x', 'y','z'])
p = Point(1,2,3)
print(p.x)
print(p.y)
print(p.z)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print (q[0])

dd = defaultdict(lambda: 'N/A' )
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key'])
dd = {'a':1, 'b':2, 'c':3}
print(dd['a'])

from collections import Counter
c = Counter()
for ch in 'Programming':
    c[ch] = c[ch] + 1
print (c)
