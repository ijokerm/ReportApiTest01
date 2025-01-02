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
import time,datetime
import datetime

# 项目当前目录 --报告生成路径
base_dir = os.path.dirname(__file__)

# 请求头管理
login_url = 'https://sh.51tagger.com/maxwell-report/rest/login'
header ={   "Content-Type": "application/json;charset=UTF-8"          }
base_url = "https://sh.51tagger.com/maxwell-report/"


userpwd = {"username":"ckadmin","password":"666666"}
res = requests.post(login_url,headers=header,json=userpwd)
token = res.json()['token']
cookies = res.cookies

# 时间组件接口
time_url = 'https://sh.51tagger.com/maxwell-report/data-api/1/picker-options'


begin = requests.get(time_url).json()[3]['begin'][0:19]

end = requests.get(time_url).json()[3]['end'][0:19]
# #当前白班次时间
# daybegin = datetime.datetime.now().strftime('%Y-%m-%d') + ' ' + begin
# dayend = datetime.datetime.now().strftime('%Y-%m-%d') + ' ' + end
# # 夜班班次时间
#
# nightend = (datetime.datetime.now()+ datetime.timedelta(days = +1)).strftime('%Y-%m-%d')+ ' ' + begin
# 日期
startdate = requests.get(time_url).json()[6]['begin'][0:10]
enddate = requests.get(time_url).json()[6]['end'][0:10]

# 生成的文件路径：文件路径配置
# 测试用例数据文件
CASE_FILE = os.path.join(base_dir,'case','testcase.xlsx')
CASE2_FILE = os.path.join(base_dir,'case','testcase2.xlsx')

# 测试用例文件
TEST_CASE = os.path.join(base_dir,'case')
# log文件路径
LOG_PATH = os.path.join(base_dir,'log','testlog.log')
# 测试报告文件路径
TEST_REPORT = os.path.join(base_dir,"report")

# 163邮箱授权码
mailcode = 'VJFDOKCVDJNKMHIV'

# print(begin)