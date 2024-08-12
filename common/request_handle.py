#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：ReportApiTest01 
@File    ：request_handle.py
@Author  ：SpringBear
@Date    ：2024/8/7 17:54 
"""

import requests
class RequestHandle:
    def __init__(self):
        """session管理器"""
        self.session = requests.session()

    def visit(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        return self.session.request(method,url, params=params, data=data, json=json, headers=headers,**kwargs)

    def close_session(self):
        """关闭session"""
        self.session.close()

# if __name__ == '__main__':

