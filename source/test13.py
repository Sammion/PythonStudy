# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 22:43:37 2017

@author: shuai.qian
"""

class student (object):
    pass

s = student()
def set_age(self, age):
    self.age = age

from types import MethodType 
s.set_a = MethodType(set_age,s)
s.set_a(19)
print (s.age)

def set_score(self, s):
    self.score  = s

student.set_score = set_score
s.set_score(100)
print (s.score)

class person (object):
    @property
    def gg(self):
        return self.__name
    @gg.setter
    def gg(self, name):
        if isinstance(name, str):
            print('name: ', name)
            self.__name = name
        else:
            print('Please input correct name!')
            
p = person()
p.gg = 'sam'
print (p.gg)





