# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 23:24:49 2017
@author: shuai.qian
"""
name = ["sam","qian","shuai"]
nid = [1, 2, 3]
d = {"sam":1, "qian":2, "shuai":3 , "qian":4}
print ('key is qian :',d['qian'])

s = set([1,2,3,4,1,2,3,4])
m = s
s.remove(4)
print (s)
s.add(6)
s.add(5)
print ('s is ', s)
print('m is ', m)

n = m & s

print (n )
print('=================')
sl = set(nid)
print(sl)