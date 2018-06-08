# -*- coding: utf-8 -*-
"""
Created on 2018/5/10

@author: Samuel
@Desc: Test get information from wiki by cookie.
@dependence: Noting
"""
import urllib.error, urllib.request, urllib.parse
import http.cookiejar
from bs4 import BeautifulSoup

LOGIN_URL = ''
tb_name = "XXXXXXXXXXXXXXXX"
# the url need to visit
# get_url = 'https://wiki.vip.corp.ebay.com/display/DW/'
get_url = 'https://wiki.vip.corp.com/display/DW/{tb}'.format(tb=tb_name)
values = {'os_username': 'user', 'os_password': 'password'}
postdata = urllib.parse.urlencode(values).encode()
user_agent = r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36' \
             r' (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
# save cookie to local file and named cookie.txt
cookie_filename = 'config/cookie.txt'
cookie_aff = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie_aff)
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(LOGIN_URL, postdata, headers)
try:
    response = opener.open(request)
except urllib.error.URLError as e:
    print(e.reason)

cookie_aff.save(ignore_discard=True, ignore_expires=True)

for item in cookie_aff:
    print('Name =' + item.name)
    print('Value =' + item.value)
# use cookie login Wiki
get_request = urllib.request.Request(get_url, headers=headers)
get_response = opener.open(get_request)
html = get_response.read()
with open(tb_name + ".html", "a", encoding='utf-8') as fw:
    fw.write(html.decode('UTF-8'))
soup = BeautifulSoup(html, 'lxml')
li_list = soup.find_all('li')

for i in li_list:
    print("li text: " + i.text)

# print()
