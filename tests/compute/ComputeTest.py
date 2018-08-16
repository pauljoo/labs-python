# -*- coding:utf-8 -*-
import unittest

from python_sample.compute.Compute import *


class Test(unittest.TestCase):
    def testCompute(self):
        compute1 = Compute()
        self.assertEqual(3, compute1.compute(1, 2))


if __name__ == '__main__':
    unittest.main()
