#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: TaylorTaurus
@contact: taylortaurus0517@gmail.com
@site: https://taylortaurus.top
@software: PyCharm
@file: login.py
@time: 2018/9/16 22:18
"""

from urllib.request import urlopen
import re

# 打开网页
to_spider_site = "https://taylortaurus.top/"
#to_spider_site = "https://morvanzhou.github.io/static/scraping/basic-structure.html"
spider_html = urlopen(to_spider_site).read().decode('utf-8')
print(spider_html)

# 查找标题
res_title = re.findall(r"<title>(.+?)</title>", spider_html)
print("\nPage Title is:", res_title[0])

# 查找链接
res_link = re.findall(r'href="(.*?)"', spider_html)
print(res_link)


