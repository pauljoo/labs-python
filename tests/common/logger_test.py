# -*- coding:utf-8 -*-
import sys,os
sys.path.append(os.path.abspath('.'))

import unittest
from python_sample.common import logger


class Test(unittest.TestCase):
    def testBuild(self):
      logger.build("test").info("aaa")
        # self.assertEqual(3, compute1.compute(1, 2))


if __name__ == '__main__':
    unittest.main()
