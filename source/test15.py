# -*- coding: utf-8 -*-

class student(object):
    __slots__ = ('name', 'set_age', 'age')
    pass

s = student()
s.name = 'Sam'
s1 = student()
s1.name = 'Qian'
print (s.name)

def set_age(self,a):
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

print (s1.score)

