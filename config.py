#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：ReportApiTest01 
@File    ：config.py
@Author  ：SpringBear
@Date    ：2024/7/22 16:27
配置文件
请求头 信息头 cookie管理 时间控件
"""
import os
import requests
import json
# 项目当前目录 --报告生成路径
base_dir = os.path.dirname(__file__)

# 请求头管理
login_url = 'https://www.51tagger.com/maxwell-report/rest/login'
header ={   "Content-Type": "application/json;charset=UTF-8"          }
base_url = "https://www.51tagger.com/maxwell-report/"


userpwd = {"username":"ckadmin","password":"401155"}
res = requests.post(login_url,headers=header,json=userpwd)
token = res.json()['token']
cookies = res.cookies

# 时间组件接口
time_url = 'https://www.51tagger.com/maxwell-report/data-api/1/picker-options'
# 当前班次时间
curbegin = requests.get(time_url).json()[3]['begin'][0:19]
curend = requests.get(time_url).json()[3]['end'][0:19]
# 日期
startdate = requests.get(time_url).json()[6]['begin'][0:10]
enddate = requests.get(time_url).json()[6]['end'][0:10]

#
# print(token)
print(curbegin)