# -*- coding:utf-8 -*-
"""
日志处理模块
@author: PaulJiang
@contact: jianghuiyao@outlook.com
"""
import logging

def build(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger
