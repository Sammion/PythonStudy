# @author Sam
# @date 2018-01-21
# desc 常见内建模块学习（二）
# collections是Python内建的一个集合模块，提供了许多有用的集合类。

from collections import namedtuple

point = namedtuple('point1', ['x', 'y'])
p = point(1,2)
print(p)
print(p.x)
print(p.y)