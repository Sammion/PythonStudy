# @author Sam
# @date 2018-01-21
# desc 常见内建模块学习（二）
# collections是Python内建的一个集合模块，提供了许多有用的集合类。

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

point = namedtuple('point1', ['x', 'y'])
p = point(1, 2)
print(p)
print(p.x)
print(p.y)
print(isinstance(p, point))
print(isinstance(p, tuple))

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# 要保持Key的顺序，可以用OrderedDict。
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('c', 2), ('z', 3), ('i', 4), ('h', 5)])
print(od)
print(od.keys())
print(('a', 1) in od.items())


# 用OrderDict可以是FIFO的队列
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set: ', (key, value))
        else:
            print('add: ', (key, value))
        OrderedDict.__setitem__(self, key, value)


luod = LastUpdateOrderedDict(4)
print(isinstance(luod, dict))
luod['c'] = 21
luod['a'] = 22
luod['d'] = 23
luod['e'] = 24
luod['c'] = 24
print(luod.items())
# last=True 是栈， last=False是先进先出队列
luod.popitem(last=False)
print(luod.items())

# Counter是一个简单的计数器，例如，统计字符出现的个数
c = Counter()
for ch in 'programing':
    c[ch] = c[ch] + 1
print(c)