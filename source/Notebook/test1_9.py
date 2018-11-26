# -*- coding: utf-8 -*-
"""
Created on 11/26/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""

if __name__ == '__main__':
    a = 4
    b = 2
    c = 3
    d = [1, 2, 3]
    r = {'a': 13, 'c': 123, 'd': 12331}
    test = lambda x, y: x * y
    test1 = lambda c: c["d"]
    print(test(c, b))
    print(test1(r))
