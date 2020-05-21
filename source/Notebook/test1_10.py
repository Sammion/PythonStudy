# -*- coding: utf-8 -*-
"""
Created on 11/26/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""

# 针对普通的数列去除重复值
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


# 针对复杂情形的数列去除重复值
def dedupe_dict(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [1, 2, 3, 4, 1, 3, 4, 5]
    print(list(dedupe(a)))
    b = [{'x': 1, 'y': 12, 'z': 3}, {'x': 1, 'y': 12, 'z': 3}, {'x': 10, "y": 2}]
    print(list(dedupe_dict(b, key=lambda d: d['x'])))
    print(list(dedupe_dict(b, key=lambda d: (d['x'], d["y"]))))
