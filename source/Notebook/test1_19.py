# -*- coding: utf-8 -*-
"""
Created on 11/28/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""

import os

# 探测是否有Python文件
files = os.listdir()
if any(name.endswith('.py') for name in files):
    print("This is python")
else:
    print("Sorry ,nopython")

l = [2, 4, 5, 6, 2, 1]
min_l = min(a for a in l)
print(min_l)

d = [
    {'name': 'Bob', 'age': 19, 'weight': 120},
    {'name': 'Bob1', 'age': 191, 'weight': 1201},
    {'name': 'Bob2', 'age': 192, 'weight': 1202},
    {'name': 'Bob3', 'age': 193, 'weight': 1203},
    {'name': 'Bob4', 'age': 194, 'weight': 1204},

]

max_age = max(i['age'] for i in d)
print(max_age)
min_age = min(d, key=lambda s:s['age'])
print(min_age)
# 这种基于生成器的解决方案可以以迭代的方式转换数据，因此在内存使用上要高效的的多。
sum_age = sum(i['age'] for i in d)
print(sum_age)
