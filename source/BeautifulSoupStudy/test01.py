# pip install beautifulsoup4
# pip install lxml
# pip install html5lib
import urllib.request
import random
from bs4 import BeautifulSoup
import time


def RandomNO(n):
    return random.randrange(0, n, 1)


urls = ['https://blog.csdn.net/maizi1045/article/details/79664527']
browsers = ['']
IP = ['']
url = urls[0]
cnt = 0

while 1:
    menuCode = urllib.request.urlopen(url).read()  # 将网页源代码赋予menuCode
    soup = BeautifulSoup(menuCode, 'html.parser')  # 使用html解析器进行解析
    # print(soup.article)
    s = RandomNO(60)
    print(cnt, '   ', s)
    time.sleep(s)
    cnt += 1

