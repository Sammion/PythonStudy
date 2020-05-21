# @author Sam
# @date 2018-01-16
# desc 再学Python的线程与进程（二）
# Windows下创建进程池

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.02f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    # 调用Join之前必须先调用close，close之后就不能继续添加新的process
    p.close()
    # 等待池内所有子进程执行完毕
    p.join()
    print('All subprocess done.')