# @author Sam
# @date 2018-02-26
# desc Python中的单例模式
#

# Python本身就是一个单例模式，
# 在导入模块时会生成pyc后缀的文件，当第二次调用该模块时不会再生成新的pyc文件，而是直接使用之前的文件。

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton,cls).__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton):
    a = 1

one = MyClass()
two = MyClass()
print(one == two)
print(id(one), id(two))

from functools import wraps

def Singleton2(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@Singleton2
class MyClass2(object):
    a = 1
one = MyClass2()
two = MyClass2()
print(one == two)
print(id(one), id(two))

class Singleton3(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton3, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass3(metaclass=Singleton3):
    pass

one = MyClass3()
two = MyClass3()
print(one == two)
print(id(one), id(two))