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
from bs4 import BeautifulSoup

# # 打开网页
# to_spider_site = "https://xlab.taylortaurus.top/"
# # to_spider_site = "https://morvanzhou.github.io/static/scraping/basic-structure.html"
# spider_html = urlopen(to_spider_site).read().decode('utf-8')
# print("spider_html is:", spider_html)
#
# # 查找标题
# res_title = re.findall(r"<title>(.+?)</title>", spider_html)
# print("\nres_title is:", res_title[0])
#
# # 查找链接
# res_link = re.findall(r'href="(.*?)"', spider_html)
# print("\nres_link is:", res_link)
#
# # 美丽汤获取div
# spider_soup = BeautifulSoup(spider_html, features='lxml')
# print("\nspider_soup:", spider_soup.div)
#
# # 获取a tag里的链接
# spider_a_link = spider_soup.find_all('a')
# spider_a_link = [l['href'] for l in spider_a_link]
# print("\nspider_a_link is:", spider_a_link)

#####以下使用示例站点da

sample_url="https://morvanzhou.github.io/static/scraping/list.html"
sample_html=urlopen(sample_url).read().decode('utf-8')
print("sample_html",sample_html)




