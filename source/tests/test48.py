# @author Sam
# @date 2018-01-17
# desc 再学Python的线程与进程（五）
# 多线程的锁
# 因为Python的线程虽然是真正的线程，
# 但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
# 任何Python线程执行前，必须先获得GIL锁，
# 然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
# 这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
# 所以，多线程在Python中只能交替执行，
# 即使100个线程跑在100核CPU上，也只能用到1个核。
# Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。 多个Python进程有各自独立的GIL锁，互不影响

import threading, os, time


def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance = balance + n
    time.sleep(3)
    # print('%s Add. balance = %f' % (threading.current_thread().name, balance))
    balance = balance - n


balance = 0
lock = threading.Lock()


def run_thread(n):
    for i in range(100):
        # 获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()


t1 = threading.Thread(target=run_thread(12), name='t1')
t2 = threading.Thread(target=run_thread(22), name='t2')
t1.start()
t2.start()
t1.join()
t2.join()
