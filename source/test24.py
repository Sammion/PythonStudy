# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:03:25 2017

@author: shuai.qian
"""

from multiprocessing import Process, Pool
import os, time, random
#子进程要执行的代码
def run_proc(name):
    print ("Run child process %s (%s)"% (name, os.getpid()))

def long_time_task(name):
    print ('Run task %s (%s)......' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*10)
    end = time.time()
    print ('Task %s runs %0.2f seconds!' % (name, (end-start)))
    
    
if __name__ == "__main__":
    print ("Prarent process %s." % os.getpid())
    pl = Pool(50)
    for i in range(10):
        pl.apply_async(long_time_task, args = (i,))
    print('Waiting for all subprocesses done...')
    pl.close()
    pl.join()
    print ('All subprocesses done.')
#    p = Process(target = run_proc, args = ('test', ))
    
#    print ('Child process will start!')
#    p.start()
#    p.join()
#    print('Child process end!')
        