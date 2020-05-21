# @author Sam
# @date 2018-01-21
# desc 再学装饰器（二）
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。


import functools, time


# 带参数的装饰器
def test_dec(text):
    def dec(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.clock()
            tmp = func(*args, **kwargs)
            end_time = time.clock()
            print('Text is %s' % text)
            print('%s runs %0.4f' % (func.__name__, (end_time - start_time)))
            return tmp

        return wrapper

    return dec


# 不带参数的装饰器
def test_ccc(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('tste')
        return func(*args, **kwargs)

    return wrapper


@test_ccc
def ccc(n):
    tmp = 1
    for i in range(1, n):
        tmp /= i
    print('Game over! & tmp is %0.6f' % tmp)


ccc(100)


@test_dec('Min')
def now():
    tmp = 1
    for i in range(1, 10000000):
        tmp /= i


now()
# if __name__ == '__main__':
# print(now('min'))
