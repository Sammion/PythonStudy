# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 23:08:08 2017
@author: shuai.qian
"""

age = input('Please input your age: ')
#Python中条件判断，首先需要注意的缩进，再就是if 和else 行末的冒号。
age = int(age)
if age >= 18 :
     print ('Your age is ', age)
     print ('Adult')
else :
     print ('Teenager')
#需要多重判断时使用elif，它是else if的缩写，同样行末需要加冒号
list_name = ['sam', 'yoka']
for name in list_name:
     print('name is ',name)
     
l  = list(range(101))
sum = 0
for i in l:
    sum = sum + i
print ('Sum is ',sum)
sum = 0
j = 1
while j < 100:
    if sum > 100:
        break
    else:
        sum = sum + j
    j = j+1
    print ("j = ",j)
