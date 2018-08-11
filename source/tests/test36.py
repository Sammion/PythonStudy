# Created on 2017-12-02
# @author：Sam
# @description：
# 学习使用Urllib

import urllib
import urllib.request
from collections import deque

data = {}
data['word'] = '天合光能'
# 用Python的urllib.parse库对普通字符串转符合url的字符串.
url_values = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
ful_url = url + url_values
# 用Python的urllib.request库抓取指定url的页面;
data = urllib.request.urlopen(ful_url).read()
data = data.decode('UTF-8')
# print(data)
# 高性能pop出列表中的值
queue = deque(['Sam', 'Tom'])
queue.append('Jack')
queue.append('fisher')
print(queue)
print(queue.popleft())
print(queue.pop())
print(queue)

# 集合运算，
a = set('abracadabra')
b = set('alacazam')
# 不同时包含于a和b的元素
print(a ^ b)
# 集合a或b中包含的所有元素
print(a | b)
# 集合a和b中都包含了的元素
print(a & b)
# 集合a中包含元素而b中没有的
print(a - b)