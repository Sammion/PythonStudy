# @author Sam
# @date 2018-01-22
# desc 常见内建模块学习（五）
# itertools提供了非常有用的用于操作迭代对象的函数。

import itertools

# 计数迭代器
natuals = itertools.count(1)
# 循环无限迭代器
cs = itertools.cycle('ABC')
# 重复n次的迭代器
ns = itertools.repeat('A', 4)
# for n in natuals:
#     print(n)

# for s in ns:
#     print(s)

# takewhile()等函数根据条件判断来截取出一个有限的序列
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)
# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))


# 计算圆周率
def pi(N):
    x = itertools.count(1, 2)
    ns = list(itertools.takewhile(lambda y: y <= 2 * N - 1, x))
    nc = itertools.cycle([4, -4])
    result = [next(nc) / i for i in ns]
    return sum(result)


if __name__ == '__main__':
    print(pi(100000))
