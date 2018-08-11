#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, threading, datetime
from bs4 import BeautifulSoup
import random
import urllib
import re
from src.BeautifulSoupStudy.file_handler import *

"""
1、抓取快代理网站的代理ip
2、并根据指定的目标url,对抓取到ip的有效性进行验证
3、最后存到指定的path
"""


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
    # headers = getheaders()  # 定制请求头
    # proxies = {"http": "http://" + ip, "https": "http://" + ip}  # 代理ip
    try:
        # print("TRY===---------------------------------------->",ip)
        proxy_support = urllib.request.ProxyHandler("https://" + ip)
        # 创建Opener
        opener = urllib.request.build_opener(proxy_support)
        # 安装OPener
        urllib.request.install_opener(opener)
        # 使用自己安装好的Opener
        response = urllib.request.urlopen(targeturl)
        # # 读取相应信息并解码
        html = response.read()
        return True

        # response = requests.get(url=targeturl, proxies=proxies, headers=headers, timeout=5).status_code
        # print("Response: ", response)
        # if response == 200:
        #     return True
        # else:
        #     return False
    except:
        return False


# -------------------------------------------------------获取代理方法----------------------------------------------------
# 免费代理 XiciDaili
def grap_ip(ip_type, target_url, file_path):  # ip类型,页码,目标url,存放ip的路径
    list = {0: 'http://www.data5u.com/free/gngn/index.shtml',  # 国内高匿代理
            1: 'http://www.data5u.com/free/gnpt/index.shtml',  # 国内普通代理
            2: 'http://www.data5u.com/free/gwgn/index.shtml',  # 国外高匿代理
            3: 'http://www.data5u.com/free/gwpt/index.shtml'  # 国外普通代理
            }

    url = list[ip_type]  # 配置url

    headers = getheaders()  # 定制请求头
    html = requests.get(url=url, headers=headers, timeout=5).text
    soup = BeautifulSoup(html, 'lxml')
    # with open("tmp.html",'a',encoding="UTF-8") as f:
    #     f.record_ip(str(soup))
    # print(soup)
    # all_ips = soup.find_all(text=re.compile('(?=(\b|\D))(((\d{1,2})|(1\d{1,2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{1,2})|(2[0-4]\d)|(25[0-5]))(?=(\b|\D))'))
    all_ips = soup.find_all(class_="l2")
    # print(all_ips)
    for i in all_ips:
        # print("\n\n===============================================================\n",i)
        t = i.find_all('li')
        if len(t) != 0:
            ip = t[0].text
            port = t[1].text
            ip = ip + ':' + port
            print('抓取到的IP和端口是：', ip)
            if checkip(target_url, ip):
                with open(path, 'a') as f:
                    f.write(ip)
                print(ip)
            else:
                record_ips(path=file_path, text=ip)


# 多线程抓取ip入口---------------------------------------------------
def grab_multi_process(target_url, file_path):
    truncate_file(file_path)  # 爬取前清空文档
    start = datetime.datetime.now()  # 开始时间
    threads = []
    for i in range(4):  # 四种类型ip
        t = threading.Thread(target=grap_ip, args=(i, target_url, file_path))
        threads.append(t)
    print('开始爬取代理ip')
    for s in threads:  # 开启多线程爬取
        s.start()
    for e in threads:  # 等待所有线程结束
        e.join()
    print('爬取完成')
    end = datetime.datetime.now()  # 结束时间
    diff = gettimediff(start, end)  # 计算耗时
    ips = read_ips(path)  # 读取爬到的ip数量
    print('一共爬取代理ip: %s 个,共耗时: %s \n' % (len(ips), diff))


# -------------------------------------------------------启动-----------------------------------------------------------
if __name__ == '__main__':
    path = 'config/data5u_ips.lis'  # 存放爬取ip的文档path
    targeturl = 'https://blog.csdn.net/maizi1045/article/details/79455347'  # 验证ip有效性的指定url
    grab_multi_process(targeturl, path)
