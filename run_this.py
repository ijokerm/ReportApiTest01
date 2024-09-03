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
from BeautifulReport import BeautifulReport
from common.send_mail import send_email_with_attachment
"""
通过该类defaultTestLoader下面的discover()方法，可自动更具测试目录start_dir匹配查找测试用例文件（test*.py），
并将查找到的测试用例组装到测试套件
"""



now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
now_path = os.path.dirname(os.path.realpath(__file__)) # 获取当前路径




def run_case():
    # 测试报告
    test_suite = unittest.defaultTestLoader.discover(config.TEST_CASE,pattern='test_*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='接口自动化测试报告', report_dir='./report')
#LOG日志记录
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename= config.LOG_PATH ,
                        filemode='w')
    logger = logging.getLogger()
    logger.info(test_suite)

    send_email_with_attachment(
        'fivemsbear@163.com',  # 发件人邮箱
        ['2013099087@qq.com', '2574284191@qq.com'],  # 收件人邮箱
        config.mailcode,  # 发件人邮箱密码
        config.TEST_REPORT + './测试报告.html',  # 附件路径
        '测试报告.html',  # 附件名称
        '测试邮件发送',  # 邮件主题
        '测试报告已添加至附件'  # 邮件正文
    )








if __name__ == '__main__':
    run_case()

