#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：ReportApiTest01 
@File    ：run_this.py
@Author  ：SpringBear
@Date    ：2024/8/9 16:55
在这里运行所有用例，并且生成报告
结果邮件发送
"""

import unittest
import config
import os
import time,datetime
import logging
from logging import handlers
from unittestreport import TestRunner
from common import HTMLTestRunner

"""
 7     通过该类defaultTestLoader下面的discover()方法
 8     可自动更具测试目录start_dir匹配查找测试用例文件（test*.py），
 9     并将查找到的测试用例组装到测试套件
10     """



now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
now_path = os.path.dirname(os.path.realpath(__file__)) # 获取当前路径

def load_case(casepath= config.case_file,rule="test*.py"):
    discover = unittest.defaultTestLoader.discover(casepath,pattern=rule)
    return discover


def run_case():
    test_suite = unittest.defaultTestLoader.discover(config.case_file,pattern='test_*.py')

    suite = unittest.TestSuite(test_suite)

    runner = TestRunner(suite,  # 测试套件对象
                        filename=config.base_dir + '/report/unittest01.html',  # 测试报告文件
                        title="测试框架是否可行",
                        tester="春天的熊",
                        desc="V1.0",
                        templates=1)  # 报告的模板



    runner.run()

if __name__ == '__main__':
    run_case()

