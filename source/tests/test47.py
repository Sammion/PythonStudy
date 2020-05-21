# @author Sam
# @date 2018-01-17
# desc 再学Python的线程与进程（四）
# 多线程

import time, threading, os


# 新线程执行的代码
def loop(num):
    print('thread %s is running...' % threading.current_thread().name)
    for n in range(num):
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance = balance + n
    time.sleep(3)
    # print('%s Add. balance = %f' % (threading.current_thread().name, balance))
    balance = balance - n


def run_thread(m):
    for i in range(100):
        # print('%s is changing balance.' % threading.current_thread().name)
        change_it(m)


if __name__ == '__main__':
    print('Process %s is running...' % os.getpid())
    t = threading.Thread(target=run_thread, name='Loop_Thread', args=(5,))
    t.start()
    t.join()
    print('Thread %s ended.' % threading.current_thread().name)

    print('==================> 我是分割线 <==================')
    balance = 0
    t1 = threading.Thread(target=run_thread, name='T1111', args=(11,))
    t2 = threading.Thread(target=run_thread, name='T2222', args=(21,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
