# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 10:16:36 2017
@author: shuai.qian
"""
import math

#函数
def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else :
        return -x
print (my_abs(-11))

#
def move (x,y,step, angle = 0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx,ny
print (move(100,100,60,math.pi/6))

def power(x,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s*x
    return s

print (power(5,2))


def register (name ,gender = "M", age = 28, city = "chang zhou"):
    print ("name is ", name)
    print ("gender is ", gender)
    print ("age is ", age)
    print ("City is ", city)
          
register ("qianshuai",age = 25, city = "Tian jing")
L = ["qian",12,13,"shuai"]
def add_end( L = []):
    L.append("END")
    return L
print (add_end())
print (add_end())
print (add_end(L))
print (add_end(L))
print("=================================")
def add_end_new( L = []):
    if L is None:
        L = []
    L.append("END")
    return L
print (add_end_new())
print (add_end_new()) 
print (add_end_new())
print (add_end_new())   
    
    
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum 
m = [1, 2, 4]
t = {1,2,3,4}
#print (calc(m))
print (calc(*m))  

dd = {'gender':'woman','city':"Changzhou","Job":"Engeer"}
def person (name, age, **kw):
    print("info of person: name is ",name, "age is ", age, "other is ", kw )
person ("sam", 26, score = 2)
person ("qian", 24, gender = 'man', city = 'Tian jin')
person ("shaui",255, **dd)
    
#
# 关键参数的另一种写法
print ('==============================================================')
def person1(name, age, *, city = 'Nanjing', job):
        print(name, age, city, job)
        
print (person1("sam", 25, city = 'Beijing', job = 'Engineer'))
print ('==============================================================')

# 可变参数的另一种写法      
print ('==============================================================')
def person1(name, age, *args, city = 'Nanjing', job):
        print(name, age, args, city, job)
        
print (person1("sam", 25, *t, city = 'Beijing', job = 'Engineer'))
print ('==============================================================')
        



















    
    
    