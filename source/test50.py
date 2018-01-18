# @author Sam
# @date 2018-01-17
# desc 再学装饰器（一）
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

import os, time


def log(func):
    def wrapper(*args, **kw):
        print('Call %s ():' % func.__name__)
        return func(*args, **kw)
        print('End')

    return wrapper


@log
def now():
    print('2018-01-18 19:54')


def run_time(func):
    def deco(*args, **kwargs):
        start = time.clock()
        print('start at ', start)
        r = func(*args, **kwargs)
        end = time.clock()
        print('end at ', end)
        runtime = end - start
        print('%s runs %0.4f s' % (func.__name__, runtime))
        return end
    return deco


@run_time
def long_func():
    tmp = 1000000
    for i in range(1, 10000000):
        tmp /= i


if __name__ == '__main__':
    # long_func = run_time(long_func)
    long_func()
