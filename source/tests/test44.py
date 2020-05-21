# @author Sam
# @date 2018-01-16
# desc 再学Python的线程与进程（一）
# Windows下创建单个进程

from multiprocessing import Process
import os

def run_proc(name):
    print("Run child process %s (%s)..."%(name,os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print("Child process wil start.")
    p.start()
    # 等待子进程结束后继续往下执行
    p.join()
    print('Child process end.')