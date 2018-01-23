# @author Sam
# @date 2018-01-23
# desc 常见内建模块学习（五）
# 上下文管理contextlib

from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("ERROR!")
        else:
            print('End')

    def query(self):
        print('Query info about %s ...' % self.name)


class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query2(name)
    yield q
    print('End')


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)


if __name__ == '__main__':
    with Query('Bob') as q:
        q.query()

    with create_query('Tom') as q:
        q.query()
    # with语句首先执行yield之前的语句，因此打印出<h1>；
    # yield调用会执行with语句内部的所有语句，因此打印出hello和world；
    # 最后执行yield之后的语句，打印出</h1>。
    with tag('h1'):
        print('Hello')
        print('world')
