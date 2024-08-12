#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：ReportApiTest01 
@File    ：run_this.py
@Author  ：SpringBear
@Date    ：2024/8/9 16:55
在这里运行所有用例，并且生成报告
打印出日志，执行记录
"""

import unittest
import config
import time,datetime

# 生成当前时间
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 测试报告：
rep_file = config.base_dir + '/report/' + now + r'Test01.html'
