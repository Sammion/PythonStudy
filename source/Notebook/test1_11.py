# -*- coding: utf-8 -*-
"""
Created on 11/26/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""
a = [1, 2, 34, 4, 543, 1231, 3, 543, 32]
# slice 可以记住切片的位置
s = slice(2, 8,2)
print(a[2: 8])
print(a[s])
print(s.start)
print(s.stop)
print(s.step)
