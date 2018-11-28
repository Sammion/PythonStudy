# -*- coding: utf-8 -*-
"""
Created on 11/27/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com',joined='2018-11-10')
print(sub.addr)
