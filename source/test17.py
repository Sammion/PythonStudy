# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 20:05:29 2017

@author: shuai.qian
"""

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda:25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
    

s = Student('Sam')

print (s)
print (Student('Michael'))
print ("====================我是分割线========================================")
print (s.age)
#print (s.score)
print ("====================我是分割线========================================")




class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a +self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        if isinstance (n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance (n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b, a+b
            return L
             
        
        
        
    
f = Fib()
print (type(Fib))
print ("====================我是分割线========================================")

print (type(f))
print ("====================我是分割线========================================")
print (f[0])
print (f[1])
print (f[2])
print ("====================我是分割线========================================")
print (f[:9])
print ("====================我是分割线========================================")

for n in Fib():
    print(n)
print ("====================我是分割线========================================")

class Chain(object):
    def __init__(self, path = 'C:'):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
    def __call__(self):
        print('My name is %s.' % self._name)
print (Chain().start.user.timeline.list)
c = Chain('Sam')
print (c())





















