# -*- coding: utf-8 -*-
"""
Created on 11/26/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "User( {} )".format(self.user_id)


Users = [User(112), User(12), User(10)]
print(Users)

# 按照对象的某一个属性进行排序，使用lambda方法获取对象属性值，性能不好
u = sorted(Users, key=lambda x: x.user_id)
print(u)

# 使用arrtgetter获取对象属性值
from operator import attrgetter
x = sorted(Users, key=attrgetter('user_id'))
print(x)