# -*- coding: utf-8 -*-
"""
Created on 11/27/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""

from collections import namedtuple

# 命名元祖，主要为了摆脱通过位置获取数据的限制。
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', joined='2018-11-10')
print(sub.addr)


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


from collections import namedtuple

Stock = namedtuple('ADC', ['name', 'shares', 'price'])


# 这种方式要比字典更加节省空间，遇到大型数据集时首选
def compute_cost(records):
    total = 0.0
    for r in records:
        s = Stock(*r)
        total += s.shares * s.price
        print(total)

    return total


if __name__ == '__main__':
    dd = namedtuple('ADC', ['name', 'shares', 'price'])
    data1 = dd('sam', 12, 10)
    data2 = dd('Bob', 11, 10)
    dat = [data1, data2]
    compute_cost(dat)
    # 但是这种方式是不可变的元祖，每次修改需要调用实例的_replace()方法进行更改
    data1._replace(shares=3)
    d = {'name': "Amy", "shares": 16, "price": 120}
    data2 = data2._replace(**d)
    print(data2)
