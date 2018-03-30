import random
import time
import requests
import urllib
from urllib import request
from bs4 import BeautifulSoup
import requests, threading, datetime
from bs4 import BeautifulSoup
import random

"""
1、从指定文件中获取代理IP
4、随机访问博客
"""

# ------------------------------------------------------文档处理--------------------------------------------------------
# 写入文档
def write(path, text):
    with open(path, 'a', encoding='utf-8') as f:
        f.writelines(text)
        f.write('\n')


# 清空文档
def truncatefile(path):
    with open(path, 'w', encoding='utf-8') as f:
        f.truncate()


# 读取文档
def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        txt = []
        for s in f.readlines():
            txt.append(s.strip())
    return txt


# ----------------------------------------------------------------------------------------------------------------------
# 计算时间差,格式: 时分秒
def gettimediff(start, end):
    seconds = (end - start).seconds
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    diff = ("%02d:%02d:%02d" % (h, m, s))
    return diff


# ----------------------------------------------------------------------------------------------------------------------
# 返回一个随机的请求头 headers
def getheaders():
    user_agent_list = [ \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    UserAgent = random.choice(user_agent_list)
    headers = {'User-Agent': UserAgent}
    return headers


# -----------------------------------------------------检查ip是否可用----------------------------------------------------
def checkip(targeturl, ip):
    headers = getheaders()  # 定制请求头
    proxies = {"http": "http://" + ip, "https": "http://" + ip}  # 代理ip
    try:
        response = requests.get(url=targeturl, proxies=proxies, headers=headers, timeout=5).status_code
        if response == 200:
            return True
        else:
            return False
    except:
        return False


# -------------------------------------------------------获取代理方法----------------------------------------------------
# 免费代理 XiciDaili
def findip(type, pagenum, targeturl, path):  # ip类型,页码,目标url,存放ip的路径
    list = {'1': 'http://www.xicidaili.com/nt/',  # xicidaili国内普通代理
            '2': 'http://www.xicidaili.com/nn/',  # xicidaili国内高匿代理
            '3': 'http://www.xicidaili.com/wn/',  # xicidaili国内https代理
            '4': 'http://www.xicidaili.com/wt/'}  # xicidaili国外http代理
    url = list[str(type)] + str(pagenum)  # 配置url
    headers = getheaders()  # 定制请求头
    html = requests.get(url=url, headers=headers, timeout=5).text
    soup = BeautifulSoup(html, 'lxml')
    all = soup.find_all('tr', class_='odd')
    for i in all:
        t = i.find_all('td')
        ip = t[1].text + ':' + t[2].text
        is_avail = checkip(targeturl, ip)
        if is_avail == True:
            write(path=path, text=ip)
            print(ip)


# 多线程抓取ip入口---------------------------------------------------
def getip(targeturl, path):
    truncatefile(path)  # 爬取前清空文档
    start = datetime.datetime.now()  # 开始时间
    threads = []
    for type in range(4):  # 四种类型ip,每种类型取前三页,共12条线程
        for pagenum in range(3):
            t = threading.Thread(target=findip, args=(type + 1, pagenum + 1, targeturl, path))
            threads.append(t)
    print('开始爬取代理ip')
    for s in threads:  # 开启多线程爬取
        s.start()
    for e in threads:  # 等待所有线程结束
        e.join()
    print('爬取完成')
    end = datetime.datetime.now()  # 结束时间
    diff = gettimediff(start, end)  # 计算耗时
    ips = read(path)  # 读取爬到的ip数量
    print('一共爬取代理ip: %s 个,共耗时: %s \n' % (len(ips), diff))




# 读取可用代理IP到列表
def read_IPs(path='ip.txt'):
    with open(path, 'r', encoding='utf-8') as f:
        IPs = []
        for s in f.readlines():
            IPs.append(s.strip())
    return IPs


# 获取随机数
def RandomNO(n):
    return random.randrange(3, n, 1)


# 直接访问
def visit_directly(headers, url, proxy_IP):
    proxy_support = urllib.request.ProxyHandler(proxy_IP)
    # 创建Opener
    opener = urllib.request.build_opener(proxy_support)
    # 添加User Angent
    opener.addheaders = [('User-Agent', headers["User-Agent"])]
    # 安装OPener
    urllib.request.install_opener(opener)
    # 使用自己安装好的Opener
    response = urllib.request.urlopen(url)
    # # 读取相应信息并解码
    # html = response.read().decode("utf-8")
    # # 打印信息
    # print(html)



    # request = urllib.request.Request(url, None, headers)  # 组装GET方法的请求
    # menuCode = urllib.request.urlopen(request).read()  # 将网页源代码赋予menuCode
    # soup = BeautifulSoup(menuCode, 'html.parser')  # 使用html解析器进行解析
    # print(soup.article)


# 通过百度间接访问
def visit_indirectly():
    pass
# 使用代理服务器的直接访问
def visit_directly_agent():

    for i in range(1, 10000):
        IPs_list = read_IPs()
        # 设置Headers
        headers = {"User-Agent": random.choice(USER_AGENTS), }
        # 设置直接访问的url
        # 本次选择的博客标题
        title_current = random.choice(titles_list)
        url_direct = 'https://blog.csdn.net/maizi1045/article/details/{0}'.format(TITLES[title_current])
        # 设置代理IP

        proxy_IP = {'http': random.choice(IPs_list)}

        print('本次选择的代理IP: ', proxy_IP['http'])
        visit_directly(headers, url_direct, proxy_IP)
        # 设置休眠时长
        s = RandomNO(60)
        # 打印结果信息
        print('这是第{0}次访问，这次访问的是：{1}。将会休眠{2}秒。'.format(i, title_current, s))
        if i % 50 == 0.3:
            path = 'ip.txt'  # 存放爬取ip的文档path
            targeturl = 'https://blog.csdn.net/maizi1045/article/details/79455347'  # 验证ip有效性的指定url
            getip(targeturl, path)
        else:
            # 进入休眠
            time.sleep(s)

# 主函数
if __name__ == '__main__':
    # 代理浏览器列表
    USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]
    # len_user_agents = len(USER_AGENTS)
    # 博客关键字目录
    TITLES = {'Hive官方使用手册——命令行': '79456510',
              'Hive官方使用手册——Hive CLI': '79470146',
              'Hive官方使用手册——新Hive CLI(Beeline CLI)': '79481686',
              'Hive官方使用手册——变量替换': '79663409',
              'Hive官方使用手册——HCatalog CLI': '79663787',
              'Hive官方使用手册——Avro Files': '79664527',
              'Hive官方使用手册——ORC': '79667857',
              'Hive官方使用手册——Parquet': '79707582',
              'Hive官方使用手册——压缩数据存储格式': '79708132',
              'Hive官方使用手册——LZO 压缩': '79709919',
              'Hive官方使用手册——数据类型': '79710406',
              'Hive官方使用手册——DDL使用说明': '79724397',
              'Hive官方使用手册——目录': '79455347'}

    #  返回所有的博客标题列表
    titles_list = list(TITLES.keys())


    for i in range(1, 10000):
        IPs_list = read_IPs()
        # 设置Headers
        headers = {"User-Agent": random.choice(USER_AGENTS), }
        # 设置直接访问的url
        # 本次选择的博客标题
        title_current = random.choice(titles_list)
        url_direct = 'https://blog.csdn.net/maizi1045/article/details/{0}'.format(TITLES[title_current])
        # 设置代理IP

        proxy_IP = {'http': random.choice(IPs_list)}

        print('本次选择的代理IP: ', proxy_IP['http'])
        visit_directly(headers, url_direct, proxy_IP)
        # 设置休眠时长
        s = RandomNO(10)
        # 打印结果信息
        print('这是第{0}次访问，这次访问的是：{1}。将会休眠{2}秒。'.format(i, title_current, s))
        if i % 50 == 0.3:
            path = 'ip.txt'  # 存放爬取ip的文档path
            targeturl = 'https://blog.csdn.net/maizi1045/article/details/79455347'  # 验证ip有效性的指定url
            getip(targeturl, path)
        else:
            # 进入休眠
            time.sleep(s)


    # req = request.Request(url_direct, headers=headers)
    # context_html = request.urlopen(url_direct).read()
    # soup = BeautifulSoup(context_html, 'html.parser')

    # print(soup.find(id='article_content'))

    # 设置百度间接访问的url
    url = 'https://www.baidu.com/s?ie=UTF-8&wd={kw}'.format(kw=random.choice(titles_list))
    res = requests.get(str(url), headers=headers)
    url = res.url
