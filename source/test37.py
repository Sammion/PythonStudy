# @author：Sam
# @date:2017-12-02
# desc：
#   使用Urllib爬取第一个网站

import urllib
import re
import urllib.request
from collections import deque

queue = deque()
visited = set()

url = 'http://news.dbanotes.net'
queue.append(url)
cnt = 0
while queue:
    url = queue.popleft()
    visited |= {url}
    print('已经抓取：', str(cnt), '\n正在抓取：', url)
    cnt += 1
    urlop = urllib.request.urlopen(url)
    if 'html' not in urlop.getheader('Content-type'):
        continue
    try:
        data = urlop.read().decode('UTF-8')
    except:
        continue
    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列---》'+x)


