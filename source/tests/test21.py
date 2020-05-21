# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 08:51:35 2017
@author: shuai.qian
"""
from io import StringIO, BytesIO

f = StringIO()
f.write('hello')
f.write(' world！')
print(f.getvalue())

sio = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = sio.readline()
    if s == '':
        break
    print(s.strip())
bio = BytesIO()
bio.write('中文'.encode('utf-8'))
print(bio.getvalue())
print(bio.read())
