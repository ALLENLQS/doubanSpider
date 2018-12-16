
#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : ALLEN
# @Time    : 2018/12/16 20:21
# @File    : main.py
# @Software: PyCharm

from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(['scrapy','crawl','movie'])