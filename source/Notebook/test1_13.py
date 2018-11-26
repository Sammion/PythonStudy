# -*- coding: utf-8 -*-
"""
Created on 11/26/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""

rows = [
    {'name': "bob", 'age': 13},
    {'name': "Amy", 'age': 14},
    {'name': "sam", 'age': 18},
]

from operator import itemgetter

# 使用itemgetter根据key获取字典里的value
rows_sort_by_name = sorted(rows, key=itemgetter('name'))
rows_sort_by_age = sorted(rows, key=itemgetter('age'))
print(rows_sort_by_age)
print(rows_sort_by_name)
# 使用lambda方式获取字典的value
rows_sort_by_name = sorted(rows, key=lambda x: x["name"])
rows_sort_by_age = sorted(rows, key=lambda x: x["age"])
print(rows_sort_by_age)
print(rows_sort_by_name)

min_name = min(rows, key=itemgetter('name'))
print(min_name)


