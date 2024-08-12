#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：ReportApiTest01 
@File    ：case_ddt.py
@Author  ：SpringBear
@Date    ：2024/8/9 17:26
unittest+ddt 实现用例的封装
"""
from common.excel_handle import ExcelHandle
from common.request_handle import RequestHandle
import ddt
import unittest
import os
import config


@ddt.ddt
class Test_Api(unittest.TestCase):
    # 读取测试用例excel的数据
    excel = ExcelHandle('../case/testcase.xlsx')
    case_data = excel.read_excel('p1')

    def setUp(self) -> None:
        self.req = RequestHandle()
        login = self.req.visit('post',config.login_url,)

    def tearDown(self) -> None:
        self.req.close_session()