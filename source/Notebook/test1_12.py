# -*- coding: utf-8 -*-
"""
Created on 11/26/2018

@author: Samuel
@Desc: 
@dependence: Noting
"""

#
words = "Dapper was initially set up for hercules using spark and Ares using Hive and that was initial way these clusters were designed to be used. We will extend dapper to other clusters for both Hive and Spark. ".split(
    " ")
from collections import Counter
# 使用Counter函数统计词频
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
print(word_counts["was"])
word_counts["was"] += 1
print(word_counts["was"])

morewords = "When you verify the manifest, you can submit the onetime file to dapper task, .sql file will be submitted when you click the TD button, and .hql/_spark.sql/.sh will be submitted when you click the HD button.".split(
    " ")

# Counter对象可以进行加减运算
morewords_counter = Counter(morewords)
print(word_counts)
print(morewords_counter)
c = morewords_counter + word_counts
print(c)
d = morewords_counter - word_counts
print(d)
