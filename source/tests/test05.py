# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 15:30:52 2017
@author: shuai.qian
"""
def fact (n):
    if n == 1:
        return 1
    return n*fact(n-1)

print (fact(10))

def move (n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move (n-1, a, c, b)
        move (1, a, b, c)
        move (n-1, b, a, c)
        print ('=====================')
   
move (4,'A','B','C')