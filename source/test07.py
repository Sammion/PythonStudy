# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:42:24 2017
@author: shuai.qian
"""

L = [d for d in range(1, 100) if d % 3 == 0]
g = (d for d in range(1, 100) if d % 3 == 0)
print(L)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('======================><======================')


# 斐波拉切数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(10)


def odd():
    print('Step 1')
    yield 1
    print('Step 2')
    yield (2)
    print('Step 3')
    yield (3)
o = odd()

print('======================><======================')
for n in fib(10):
    print(n)


def triangles(lines):
    L = [1]
    n = 0
    while n < lines:
        yield L
        L1 = [1]
        for i in range(0, len(L) - 1):
            L1.append(L[i] + L[i + 1])
            i = i + 1
        L1.append(1)
        L = L1
        n = n + 1


for n in triangles(10):
    print(n)


def add(a, b, f):
    return f(a) + f(b)
f = abs
print(add(1, -2, f))
