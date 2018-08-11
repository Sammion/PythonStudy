# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:30:27 2017
@author: shuai.qian
"""


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, v):
        if not isinstance(v, int):
            raise ValueError('score must be an interge')

        elif v < 0 or v > 100:
            raise ValueError('score must be between 0 and 100')
        self._score = v

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        self._height = h

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, w):
        self._width = w

    @property
    def resolution(self):
        return self._resolution

    @resolution.setter
    def resolution(self, value):
        self._resolution = value


s = Student()
s.score = 99
print(s.score)
print("====================我是分割线========================================")

s.width = 1024
s.height = 768

s.resolution = 786432
print('1024 * 768 = %d ?' % s.resolution)
print(s.resolution)
