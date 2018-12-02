# -*- coding: utf-8 -*-
"""
Created on 11/28/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""
a = {'a': 1, 'b': 2, 'c': 3, 'd': 122}
b = {'d': 12, 'e': 14, 'f': 23}
from collections import ChainMap

c = ChainMap(a, b)
print(c)
print(c['d'])
print(c.values())
print(c.items())
print(c.keys())

values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])

print(values.parents)
print('=' * 33)
a = {'x': 1, 'y': 2, 'z': 33}
b = {'x': 11, 'y': 22}
# 按普通执行顺序更新
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged)
merged['x'] = 11
print(merged['x'])

print('=' * 10)
# ChainMap可以自动更新。
auto_update_dict = ChainMap(a, b)
print(auto_update_dict)
print(auto_update_dict['x'])
auto_update_dict['x'] = 100
print(auto_update_dict['x'])
