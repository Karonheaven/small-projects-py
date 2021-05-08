#!/usr/bin/env python
# coding:utf-8
"""
# 使用Selenium
# Author: Karonheaven
"""
# +---------------+需要的包+---------------+
# 标准库导入
from typing import *

# 第三方库导入
from selenium import webdriver

# 本地库/自定义库导入


# +---------------+全局变量&预定义+---------------+
driver = webdriver.Chrome()

# 添加参数
opts = webdriver.ChromeOptions()
opts.add_argument(argument="--disable-gpu")

# +---------------+主程序+---------------+
pass
