# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 10:38:35 2017

@author: shuai.qian
"""

import threading
local_school = threading.local()

def process_student():
    #
    st = local_school.student
    print ('Hello, %s (in %s)' % (st, threading.current_thread().name))
    
def process_thread(name):
    #
    local_school.student = name
    process_student()

t1 = threading.Thread(target = process_thread, args = ('Alice', ), name = 'Threa-A')
t2 = threading.Thread(target = process_thread, args = ('Bob', ), name = 'Threa-B')

t1.start()
t2.start()

t1.join()
t2.join()


    
    