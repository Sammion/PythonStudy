# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 09:41:49 2017
@author: shuai.qian
"""
import os
import pickle

f = open('E:\Company\Test\dump.txt', 'wb')
d = dict(name='Sam', age=22, score=99)
pickle.dump(d, f)
f.close()

data = None
f = open('E:\Company\Test\3-2\Paqfiles\Paqfile0\ProcessFiles\ProcessFile0\ClassData', 'rb')
print('执行我了吗！')
data = pickle.load(f)
print('有没有执行我了呢！')
f.close()

print('反序列化后', data)
