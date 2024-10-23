#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：ReportApiTest01 
@File    ：readexcel.py
@Author  ：SpringBear
@Date    ：2024/8/7 17:49
"""
# coding:utf-8
import pandas as pd
import config
import openpyxl

# 定义一个函数，用于从Excel文件中读取测试用例数据
def read_test_cases_from_excel(file_path, sheet_name):
    # 利用pandas读取Excel文件
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    # 将DataFrame转换为字典列表，每个字典代表一个测试用例
    test_cases = df.to_dict(orient='records')
    return test_cases



# 定义一个函数，用于将配置数据插入到测试用例中（如果测试用例中包含占位符）
# def replace_test_cases(test_cases):
#     params_dict = {
#         '${begintime}': config.begin,
#         '${endtime}': config.end
#     }
#
#     # 遍历每个测试用例，并替换其中的占位符
#     for test_case in test_cases:
#         for key, value in params_dict.items():








# 读取Excel文件中的测试用例数据
test_cases = read_test_cases_from_excel(config.CASE_FILE, sheet_name='p2')


# print(read_test_cases_from_excel(config.CASE_FILE,'p2')[0]['payload'])


def replace_excel_parameters(input_excel_path, sheet_name, parameters_to_replace, output_excel_path):
    """
    替换Excel表格中单元格的参数化数据值。

    :param input_excel_path: 输入Excel文件的路径。
    :param sheet_name: 要处理的Excel工作表名称。
    :param parameters_to_replace: 要替换的参数及其新值的字典，键是参数（可以是单元格值的一部分或完全匹配），值是新的单元格内容。
    :param output_excel_path: 输出Excel文件的路径。
    """
    # 加载Excel工作簿和工作表
    workbook = openpyxl.load_workbook(input_excel_path)
    sheet = workbook[sheet_name]

    # 遍历所有单元格，查找并替换参数
    for row in sheet.iter_rows():
        for cell in row:
            # 检查单元格值是否包含要替换的参数
            for param, new_value in parameters_to_replace.items():
                if isinstance(cell.value, str) and param in cell.value:
                    # 替换单元格中的参数值
                    cell.value = cell.value.replace(param, new_value)

                    # 保存修改后的工作簿
    workbook.save(output_excel_path)


# 示例用法
parameters_to_replace = {
    '${begintime}': config.begin,
    '${endtime}': config.end
}

input_excel_path = config.CASE_FILE
output_excel_path = config.CASE2_FILE
sheet_name = 'p2'

replace_excel_parameters(input_excel_path, sheet_name, parameters_to_replace, output_excel_path)
