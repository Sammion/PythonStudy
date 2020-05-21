# -*- coding: utf-8 -*-
"""
Created on 11/26/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""

rows = [
    {'addr': "shanghai", "name": "Amy", "date": "1/12/2018"},
    {'addr': "sichuan", "name": "Bmy", "date": "1/12/2018"},
    {'addr': "shanghai", "name": "Cmy", "date": "1/12/2018"},
    {'addr': "sichuan", "name": "Dmy", "date": "1/12/2017"},
    {'addr': "shanghai", "name": "Emy", "date": "1/12/2017"},
    {'addr': "henan", "name": "Fmy", "date": "1/12/2017"},
    {'addr': "henan", "name": "Gmy", "date": "1/12/2017"},
    {'addr': "shanghai", "name": "Hmy", "date": "1/12/2017"}

]

from operator import itemgetter
from itertools import groupby

# 首先需要排序，因为groupBy只能比较相邻项
rows.sort(key=itemgetter('addr'))
# 分组
for date, items in groupby(rows, key=itemgetter('addr')):
    print(date)
    for i in items:
        print("  ", i)
