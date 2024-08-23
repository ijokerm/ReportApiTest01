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
    excel = ExcelHandle('../case/testcase.xlsx')
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

        try:
            #   断言：预期结果与实际结果对比
            self.assertEqual(res.status_code,items['expect_result'])
            result = 'pass'
        except AssertionError as e:
            result = 'fail'
            raise e
        finally:
            #    将响应的状态码写入testcase.xlsx第9列
            Test_Api.excel.write_excel("../case/testcase.xlsx",'p1',items['case_id']+1,9,res.status_code)
            #   如果断言成功，则在第10列写入测试结果‘pass’，否则写入‘fail’
            Test_Api.excel.write_excel("../case/testcase.xlsx",'p1',items['case_id']+1,10,result)
        logging.info(f"什么垃圾日志打印不出来？？：{result}")

if __name__ == '__main__':
    unittest.main()


