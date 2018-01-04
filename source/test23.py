# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:38:38 2017
@author: shuai.qian
"""
import json

d = dict(name='Sam', age=20, score=88)
print(json.dumps(d))

json_str = '{"age":20, "score":99, "name":"Sam"}'
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 100)
# print (json.dumps(s))
print(json.dumps(s, default=lambda obj: obj.__dict__))


def dict2Student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2Student))
