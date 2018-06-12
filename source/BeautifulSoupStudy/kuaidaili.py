#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, threading, datetime
from bs4 import BeautifulSoup
import random
import re
from source.BeautifulSoupStudy.file_handler import *

"""
1、抓取快代理网站的代理ip
2、并根据指定的目标url,对抓取到ip的有效性进行验证
3、最后存到指定的path
"""


# ----------------------------------------------------------------------------------------------------------------------
# 计算时间差,格式: 时分秒
def gettimediff(start, end):
    seconds = (end - start).seconds
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    diff = ("%02d:%02d:%02d" % (h, m, s))
    return diff


# Check Ip is available or not.
def check_ip(targeturl, ip):

    proxies = {"http": "http://" + ip, "https": "http://" + ip}  # 代理ip
    try:
        response = requests.get(url=targeturl, proxies=proxies, timeout=5).status_code
        if response == 200:
            return True
        else:
            return False
    except:
        return False


#
def grab_ips(agent_type, page_num, targeturl, ips_file):
    url_list = {'1': 'https://www.kuaidaili.com/free/inha/',
                '2': 'https://www.kuaidaili.com/free/intr/'}
    url = url_list[str(agent_type)] + str(page_num)
    agents = get_agents()
    headers = {'User-Agent': random.choice(agents).replace('\n', '')}
    print(url)
    print(headers)
    html = requests.get(url=url, timeout=10).text
    soup = BeautifulSoup(html, 'lxml')
    all = soup.find_all('tr')
    for i in all:
        t = i.find_all('td', attrs={'data-title': re.compile("(IP)|(PORT)")})
        if len(t) != 0:
            ip = t[0].text
            port = t[1].text
            ip = ip + ':' + port
            print('抓取到的IP和端口是：', ip)
            is_avail = check_ip(targeturl, ip)
            # is_avail = True
            if is_avail:
                record_ips(path=ips_file, text=ip)
            else:
                record_ips(path=ips_file, text=ip)
                print(ip + 'does not work well.')
        else:
            print('Zero ip could be found in that website.')


# Grab ips with multi-process
def grab_multi_process(test_url, ips_file):
    truncate_file(ips_file)
    start = datetime.datetime.now()  # 开始时间
    threads = []
    for type in range(2):
        for page_num in range(1):
            t = threading.Thread(target=grab_ips, args=(type + 1, page_num + 1, test_url, ips_file))
            threads.append(t)
    print('开始爬取代理ip')
    for s in threads:  # 开启多线程爬取
        s.start()
    for e in threads:  # 等待所有线程结束
        e.join()
    print('爬取完成')
    end = datetime.datetime.now()  # 结束时间
    diff = gettimediff(start, end)  # 计算耗时
    ips = read_ips(ips_file)
    print('一共爬取代理ip: %s 个,共耗时: %s \n' % (len(ips), diff))


# -------------------------------------------------------启动-----------------------------------------------------------
if __name__ == '__main__':
    ips_file = 'config/kuaidaili_ips.lis'  # 存放爬取ip的文档path
    targeturl = 'https://blog.csdn.net/maizi1045/article/details/79455347'  # 验证ip有效性的指定url
    grab_multi_process(targeturl, ips_file)
