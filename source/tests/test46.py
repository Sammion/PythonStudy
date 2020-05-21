# @author Sam
# @date 2018-01-17
# desc 再学Python的线程与进程（三）
# 进程间通信

from multiprocessing import Process, Queue
import os, time, random


# 写数据进入进程
def write_queue(q):
    print("Process to write: %s" % os.getpid())
    for value in ['A', 'B', 'C', 'D', 'E']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读取数据
def read_queue(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get()
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write_queue, args=(q,))
    pr = Process(target=read_queue, args=(q,))
    pw.start()
    pr.start()
    # 等待写入数据结束
    pw.join()
    # pr进程时死循环，无法等待其结束，只能强行终止
    pr.terminate()
