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


# 定义一个函数，用于从Excel文件中读取测试用例数据
def read_test_cases_from_excel(file_path, sheet_name):
    # 利用pandas读取Excel文件
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    # 将DataFrame转换为字典列表，每个字典代表一个测试用例
    test_cases = df.to_dict(orient='records')
    return test_cases


# 示例：假设我们有一个配置字典，用于存储一些全局配置（本例中为开始和结束时间）
config = {
    'begin': '2023-01-01',
    'end': '2023-12-31'
}


# 定义一个函数，用于将配置数据插入到测试用例中（如果测试用例中包含占位符）
def inject_config_into_test_cases(test_cases, config):
    params_dict = {
        '${begintime}': config['begin'],
        '${endtime}': config['end']
    }

    # 遍历每个测试用例，并替换其中的占位符
    for test_case in test_cases:
        for key, value in params_dict.items():
            if key in test_case['input']:  # 假设输入参数存储在'input'键下，且为字符串
                test_case['input'] = test_case['input'].replace(key, value)
                # 如果预期结果中也包含占位符，同样进行替换
            if key in test_case['expected']:
                test_case['expected'] = test_case['expected'].replace(key, value)

                # 注意：此示例假设'input'和'expected'是字符串，并可能包含占位符。
    # 根据您的实际情况，您可能需要调整此逻辑以处理不同类型的输入和预期结果。

    # 如果输入参数不是字符串，或者存储在多个列中，您需要相应地修改此逻辑。
    # 例如，如果输入参数是两个独立的列'input1'和'input2'，则您需要分别替换它们。

    # 此外，如果测试用例数据中包含其他需要配置的字段，您也可以在此处进行替换。

    return test_cases


# 读取Excel文件中的测试用例数据
test_cases = read_test_cases_from_excel('test_cases.xlsx', 'Sheet1')

# 将配置数据插入到测试用例中（如果需要）
# 注意：此步骤取决于您的测试用例数据是否包含占位符，以及您是否希望用配置数据替换它们。
# 如果不需要此步骤，请跳过。
test_cases_with_config = inject_config_into_test_cases(test_cases, config)


# 在此之后，您可以使用`pytest`的参数化测试功能来运行这些测试用例。
# 但是，请注意，上面的`inject_config_into_test_cases`函数是一个示例，
# 并且可能需要根据您的实际测试用例数据进行调整。
# 此外，下面的`test_example`函数也只是一个示例，您需要根据您的被测试函数来编写实际的测试函数。

# 示例测试函数（需要根据实际情况进行修改）
# @pytest.mark.parametrize("test_case", test_cases_with_config)
# def test_example(test_case):
#     # 假设我们有一个被测试的函数`execute_test`，它接受输入参数并返回结果。
#     # 我们需要在这里调用它，并使用断言来检查结果是否与预期相符。
#     # 但是，由于我们没有`execute_test`函数的定义，因此下面只是一个占位符。
#     result = execute_test(test_case['input'])  # 需要替换为实际的函数调用
#     assert result == test_case[
#         'expected'], f"Test failed for input {test_case['input']}: expected {test_case['expected']} but got {result}"
#

# 注意：上面的`execute_test`函数是一个占位符，您需要用实际的被测试函数来替换它。
# 此外，您还需要确保`test_case['input']`和`test_case['expected']`与您的测试用例数据格式相匹配。
if __name__ == "__main__":
    filepath = "../case/testcase.xlsx"
    sheetName = "p1"
    data = ExcelUtil(filepath, sheetName)
    print(data.dict_data())