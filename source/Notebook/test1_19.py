# -*- coding: utf-8 -*-
"""
Created on 11/28/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""

import os
# 探测是否有Python文件
files = os.listdir()
if any(name.endswith('.py') for name in files):
    print("This is python")
else:
    print("Sorry ,nopython")

