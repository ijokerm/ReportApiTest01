#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：ReportApiTest01 
@File    ：test_p1.py
@Author  ：SpringBear
@Date    ：2024/8/9 17:26
unittest+ddt 实现用例的封装
增加日志输出
"""
import json
import unittest

import ddt

import config
from common.excel_handle import ExcelHandle
from common.request_handle import RequestHandle
import logging




@ddt.ddt
class Test_Api(unittest.TestCase):
    # 读取测试用例excel的数据
    excel = ExcelHandle(config.CASE_FILE)
    case_data = excel.read_excel('p1')

    def setUp(self) -> None:
        self.req = RequestHandle()
        login = self.req.visit('post',config.login_url,json=config.userpwd,headers=config.header)

        self.assertEqual(login.status_code,200)
    def tearDown(self) -> None:
        # 关闭session
        self.req.close_session()
    @ddt.data(*case_data)
    def test_api(self,items):
        # 请求接口
        res = self.req.visit(method=items['method'],url=config.base_url+items['url'],
                             json=json.loads(items['payload']),headers=json.loads(items['headers']))
        self.url = items['url']
        self.case_name = items['case_name']
        self.method = items['method']
        self.headers = items["headers"]
        self.body = eval(items['payload'])
        self.actual_result = items['actual_result']  # 提取字段
        self.test_result = items["test_result"]  # 获取excel表格数据的状态码
        try:
            #   断言：预期结果与实际结果对比
            self.assertEqual(res.status_code,items['expect_result'])
            result = 'pass'
        except AssertionError as e:
            result = 'fail'
            raise e
        finally:
            #    将响应的状态码写入testcase.xlsx第9列
            Test_Api.excel.write_excel(config.CASE_FILE,'p1',items['case_id']+1,9,res.status_code)
            #   如果断言成功，则在第10列写入测试结果‘pass’，否则写入‘fail’
            Test_Api.excel.write_excel(config.CASE_FILE,'p1',items['case_id']+1,10,result)
            print("******* 正在执行用例 ->{0} *********".format(self.case_name))
            print("请求方式: {0}，请求URL: {1}".format(self.method, self.url))
            print("请求数据类型为:{0} 请求header为:{1}".format(type(self.headers), self.headers))
            print("请求数据类型为:{0} 请求body为:{1}".format(type(self.body), self.body))

if __name__ == '__main__':
    unittest.main()


