# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:01:02 2017

@author: shuai.qian
"""

from enum import Enum, unique


@unique
class Weekday(Enum):
    sun = 1
    Mon = 2
    Tue = 3
    Wed = 4
    Thu = 5
    Fri = 6
    Sat = 7


day1 = Weekday.Mon
print(day1)
print(Weekday['Tue'])
print(day1 == Weekday.Mon)
print(Weekday(1))
print(day1 == Weekday(1))
print(type(day1))
for name, member in Weekday.__members__.items():
    print(name, '=>', member)

attr1 = 12
attr2 = 13


def fn(self, n):
    print('Hello, %s' % n)


Hello = type('Hello', (object,), dict(hello=fn, a=attr1, b=attr2))
h = Hello()
h.hello('world！')
print(h.a)
print(h.b)
