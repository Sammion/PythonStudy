# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 08:04:51 2017
@author: shuai.qian
"""
import logging

logging.basicConfig(level=logging.INFO)
try:
    print('Try ......')
    r = 10 / 2
    print('Result is %s' % r)
except ZeroDivisionError as e:
    print('Except:', e)
finally:
    print('Finally')
logging.info('===================我是分割线======================')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 5


def main(s):
    logging.info('s = %s' % s)
    # assert s != 0, 'n is zero!'
    try:
        bar(s)
    except Exception as e:
        logging.exception(e)
    finally:
        print('Finally! ')


main(0)
print('END')
