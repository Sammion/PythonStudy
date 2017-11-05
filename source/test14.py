# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 23:00:23 2017

@author: shuai.qian
"""
class Animal(object):
    def __init__(self, n):
        self.__name = n
        
    def run(self):
        print ("%s running!" % self.__name)

class Runnable(object):
    def __init__(self, n):
        self.__name = n
    def bark(self):
        print ('%s barking!' % self.__name)

class Flyable(object):
    
    def __init__(self, n):
        self.__name = n
    def fly(self):
        print ('%s flying!' % self.__name)

class Bird(Flyable, Animal):
    pass

class Dog(Runnable, Animal):
    pass
 

d = Dog('dd')
b = Bird('bb')
d.bark()
b.fly()
#d.run()
#b.run()
print ("====================我是分割线========================================")
print (dir(b))

print ("====================我是分割线========================================")
print (type(b))
print ("====================我是分割线========================================")
print (b.__sizeof__())


