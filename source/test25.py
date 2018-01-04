# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:35:40 2017
@author: shuai.qian
"""

import time, threading


def loop():
    print('Thread %s is running ...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(10)
    print('Thread %s ended.' % threading.current_thread().name)


print('thread %s is running ...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)
