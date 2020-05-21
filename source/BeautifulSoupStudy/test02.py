import urllib.request
import random
import urllib3
import time

def RandomNO(n):
    return random.randrange(0, n, 1)
urls = ['']
browsers = ['']

url = 'https://blog.csdn.net/maizi1045/article/details/79664527'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
refererData = 'https://www.baidu.com/link?url=iqRTVMTVveILuMDOyKo9ntxFFDzrVg_o0OJL161cTrwC35tSGeMYu21sthRsHG3QV6aG4NcSMnaJ6qsWS1eLPh-RUtEG323ulejYLrOk2xq&wd=&eqid=b28e631b0001654b000000055abc8ce6'
data = None  # 将GET方法中待发送的数据设置为空
headers = {'User-Agent': user_agent, 'Referer': refererData}  # 构造GET方法中的Header
count = 0  # 初始化计数器
request = urllib.request.Request(url, data, headers)  # 组装GET方法的请求
while 1:  # 一旦开刷就停不下来
    rec = urllib.request.urlopen(request)  # 发送GET请求，获取博客文章页面资源
    page = rec.read()  # 读取页面内容到内存中的变量，这句代码可以不要
    count += 1  # 计数器加1
    print(count)  # 打印当前循环次数
    if count % 6:  # 每6次访问为1个循环，其中5次访问等待时间为31秒，另1次为61秒
        time.sleep(10)  # 为每次页面访问设置等待时间是必须的，过于频繁的访问会让服务器发现刷阅读量的猥琐行为并停止累计阅读次数
    else:
        time.sleep(2)
        # 打印页面信息，这句代码永远不会执行
