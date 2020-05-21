# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:55:48 2017
@author: shuai.qian
"""


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 5, 6, 78, 10])))


# 计算素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break
