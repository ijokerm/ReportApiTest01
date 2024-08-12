#!/git/ijokerm
# -*- coding: UTF-8 -*-
"""
@Project ：ReportApiTest01 
@File    ：run_log.py
@Author  ：SpringBear
@Date    ：2024/7/25 11:05
定义初始化日志函数
--定义日志器/定义处理器/定义格式化器/设置处理器的格式/将处理器添加到日志器中
"""
import logging
from logging import handlers

import config


def init_log():
    # 初始化日志器对象 获取日志器
    logger = logging.getLogger()
    # 设置日志器对应日志的格式
    logger.setLevel(logging.INFO)
    # 定义处理器 --控制台处理器
    sh = logging.StreamHandler()
    # 定义处理器 --文件处理器
    log_file = config.base_dir + "/log/demo.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_file,  # 定义日志文件
                                              when="D", # 记录日志的时间--按天
                                            interval=1, #记录日志的频率
                                            backupCount=7,# 保存日志的时间
                                            encoding="UTF-8" #记录日志的编码格式
                                            ) # 文件处理器
    # 定义格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 设置处理器的格式
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)