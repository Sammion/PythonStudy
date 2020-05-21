# -*- coding: utf-8 -*-
"""
Created on 8/12/2018

@author: Samuel
@Desc: Test the module selenium
@dependence:
chromedriver.exe (need to install chrome 68.0 on your server)
Chrome browser driver download.
https://sites.google.com/a/chromium.org/chromedriver/downloads


"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome(executable_path="driver\win10X64\chromedriver.exe")
try:
    browser.get("https://www.baidu.com")
    input = browser.find_element_by_id("kw")
    # use the chrome to finish the key word search.
    input.send_keys("Python")
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "content_left")))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
    time.sleep(10)
finally:
    browser.close()
