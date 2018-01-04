# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 20:07:27 2017

@author: shuai.qian
"""
import matplotlib.pyplot as plt
from odps.df import DataFrame
from odps import ODPS

o = ODPS('',project='', endpoint='')
t = DataFrame(o.get_table('tmp_ods_mc_testing_dlt'))
print("=================================> START <==================================")
#print(t.dtypes)
#print(t["class"].head(5))
t.groupby('class').agg(count = t['class'].count())

# %matplotlib inline

t['class'].value_counts().plot(kind = 'bar', x = 'class', xlabel = 'cnt' )

tmp = range(0,10,2)
tmp.pop(1)
