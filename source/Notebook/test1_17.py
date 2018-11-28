# -*- coding: utf-8 -*-
"""
Created on 11/27/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""

prices = {
    'ACE': 45.32,
    'aapl': 23.32,
    'IBM': 37.30,
    'HPQ': 10.72,
    'FB': 90.12
}

p1 = {key: value for key, value in prices.items() if value > 70}
print(p1)
tech_name = {'ACE', 'IBM', 'HPQ'}
p2 = {key: value for key, value in prices.items() if key in tech_name}
print(p2)

p3 = dict((key, value) for key, value in prices.items() if value > 10)

