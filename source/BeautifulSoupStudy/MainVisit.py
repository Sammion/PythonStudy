import time
import urllib
from urllib import request
import requests, threading, datetime
from bs4 import BeautifulSoup
import random
import logging
from logging.config import fileConfig

fileConfig('config/Logger_config.ini')
log = logging.getLogger('mylogger')
log.info("Start programming!!!")


def read_urls(file_input, mid="="):
    res_url = dict()
    with open(file_input, 'r', encoding="UTF-8") as fr:
        lines = fr.readlines()
        for line in lines:
            if line[0] == '#':
                print("Skip line:" + line)
                continue

            name = line.split(mid)[0].strip()
            url = line.split(mid)[1].strip()
            res_url[name] = url
    return res_url


# Return a list of agents which configured in the config file.
def get_agents(agents_file='config/agents.lis'):
    agents = list()
    with open(agents_file) as fr:
        agents = fr.readlines()
        fr.close()
    return agents


def get_config(in_file, mid_word):
    res_dict = dict()
    with open(in_file, mode="r", encoding='utf-8') as fr:
        rows = fr.readlines()
        for r in rows:
            k = r.strip().replace("\\n", "").split(mid_word)
            k = k[0]
            v = k[-1]
            res_dict[k] = v
        fr.close()
    return res_dict


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


# 计算时间差,格式: 时分秒
def gettimediff(start, end):
    seconds = (end - start).seconds
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    diff = ("%02d:%02d:%02d" % (h, m, s))
    return diff


# -----------------------------------------------------检查ip是否可用----------------------------------------------------
def checkip(targeturl, ip):
    headers = get_agents()  # 定制请求头
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
    headers = get_agents()  # 定制请求头
    html = requests.get(url=url, headers=headers, timeout=5).text
    soup = BeautifulSoup(html, 'lxml')
    all = soup.find_all('tr', class_='odd')
    for i in all:
        t = i.find_all('td')
        ip = t[1].text + ':' + t[2].text
        is_avail = checkip(targeturl, ip)
        if is_avail == True:
            write(path=path, text=ip)
            log.info(ip)


# 多线程抓取ip入口---------------------------------------------------
def getip(targeturl, path):
    truncatefile(path)  # 爬取前清空文档
    start = datetime.datetime.now()  # 开始时间
    threads = []
    for type in range(4):  # 四种类型ip,每种类型取前三页,共12条线程
        for pagenum in range(3):
            t = threading.Thread(target=findip, args=(type + 1, pagenum + 1, targeturl, path))
            threads.append(t)
    log.info('开始爬取代理ip')
    for s in threads:  # 开启多线程爬取
        s.start()
    for e in threads:  # 等待所有线程结束
        e.join()
    log.info('爬取完成')
    end = datetime.datetime.now()  # 结束时间
    diff = gettimediff(start, end)  # 计算耗时
    ips = read(path)  # 读取爬到的ip数量
    log.info('一共爬取代理ip: %s 个,共耗时: %s \n' % (len(ips), diff))


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
    # Create handler
    proxy_support = urllib.request.ProxyHandler(proxy_IP)
    # 创建Opener
    opener = urllib.request.build_opener(proxy_support)
    # 添加User Angent
    opener.addheaders = [('User-Agent', headers["User-Agent"])]
    # 安装OPener
    urllib.request.install_opener(opener)
    # 使用自己安装好的Opener
    # print(url)
    response = urllib.request.urlopen(url)
    # # 读取相应信息并解码
    html = response.read()
    # # 打印信息
    # log.info(html)

    # with open("tmp.html", 'a', encoding='utf-8') as f:
    #     f.record_ip(html.decode('UTF-8'))

    # request = urllib.request.Request(url, None, headers)  # 组装GET方法的请求
    # menuCode = urllib.request.urlopen(request).read()  # 将网页源代码赋予menuCode
    # soup = BeautifulSoup(menuCode, 'html.parser')  # 使用html解析器进行解析
    # log.info(soup.article)


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

        log.info('本次选择的代理IP: ', proxy_IP['http'])
        visit_directly(headers, url_direct, proxy_IP)
        # 设置休眠时长
        s = RandomNO(60)
        # 打印结果信息
        log.info('这是第{0}次访问，这次访问的是：{1}。将会休眠{2}秒。'.format(i, title_current, s))
        if i % 50 == 0.3:
            path = 'ip.txt'  # 存放爬取ip的文档path
            targeturl = 'https://blog.csdn.net/maizi1045/article/details/79455347'  # 验证ip有效性的指定url
            getip(targeturl, path)
        else:
            # 进入休眠
            time.sleep(s)


# 主函数
if __name__ == '__main__':
    url_file = "config/urls.cfg"
    TITLES = read_urls(url_file, mid="=")

    USER_AGENTS = get_agents()
    titles_list = list(TITLES.keys())

    for i in range(1, 10000):
        IPs_list = read_IPs()
        # 设置Headers
        headers = {"User-Agent": random.choice(USER_AGENTS).replace('\n', ''), }
        # 设置直接访问的url
        # 本次选择的博客标题
        title_current = random.choice(titles_list)
        # print(title_current)
        url_direct = 'https://blog.csdn.net/maizi1045/article/details/{id}'.format(id=TITLES[title_current])
        # 设置代理IP
        proxy_IP = {'http': random.choice(IPs_list)}
        log.info('本次选择的代理IP: ' + proxy_IP['http'])
        # Visit directly
        visit_directly(headers, url_direct, proxy_IP)
        # 设置休眠时长
        s = RandomNO(60)
        # 打印结果信息
        log.info('这是第{0}次访问，这次访问的是：{1}。将会休眠{2}秒。'.format(i, title_current, s))
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

    # log.info(soup.find(id='article_content'))

    # 设置百度间接访问的url
    url = 'https://www.baidu.com/s?ie=UTF-8&wd={kw}'.format(kw=random.choice(titles_list))
    res = requests.get(str(url), headers=headers)
    url = res.url
