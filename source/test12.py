# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 21:38:50 2017

@author: shuai.qian
"""

class Student (object):
        def __init__(self, name, score):
            self.__n = name
            self.s = score
        def get_n (self):
            return self.__n
        def print_info(self):
            print('%s: %s' % (self.__n, self.s))

bart = Student('Sam',100)
lisa = Student('Lisa',99)
bart.print_info()
lisa.print_info()
print(bart.get_n())
print(bart._Student__n)
# 访问限制 属性前加两个下划线


class Animal(object):
    def run(self):
        print('Animal is running!')

class Dog (Animal):
    def run(self):
        print('Dog is running!')

a = Animal()
d  = Dog()
d.run()
print (isinstance(d, Dog))
print (isinstance(d, Animal))

def run_twice(Animal):
    Animal.run()
    Animal.run()

run_twice(a)
print (type(a))

s = '123456789'
print (len(s))
print ('================================================')
print (hasattr(a,'run' ))
print (hasattr(lisa,'s' ))
print (hasattr(lisa,'__n' ))
print (getattr(a,'run'))
setattr(lisa,'s',0)
print (lisa.s)



    

