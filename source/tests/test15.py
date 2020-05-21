# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:00:23 2017
@author: shuai.qian
"""

# 使用slots
class student(object):
    __slots__ = ('name', 'set_age', 'age')
    pass


s = student()
s.name = 'Sam'
s1 = student()
s1.name = 'Qian'
print(s.name)


def set_age(self, a):
    self.age = a


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)


def set_score(self, s):
    self.score = s


student.setScore = set_score

s.setScore(100)

s1.setScore(99)

print(s1.score)
