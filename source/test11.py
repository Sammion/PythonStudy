# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 23:19:13 2017

@author: shuai.qian
"""

def log(fun):
    def wrapper(*args, **kw):
        print('call %s():' %fun.__name__)
        return fun(*args, **kw)
    
    return wrapper

@log
def now():
    print('Hello world!')

now()