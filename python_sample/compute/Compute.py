# -*- coding:utf-8 -*-
"""
计算接口模块
@author: PaulJiang
@contact: jianghuiyao@outlook.com
"""

from python_sample.common import logger


class Compute(object):

    def compute(self, a, b):
        logger.build("compute").info("param a:%d", a)
        logger.build("compute").info("param b:%d", b)
        # PythonSample.logger().info("param a:%d", a)
        # PythonSample.logger().info("param b:%d", b)
        return a + b
