from python_sample import PythonSample


class Compute(object):

    def compute(self, a, b):
        PythonSample.logger().info("param a:%d", a)
        PythonSample.logger().info("param b:%d", b)
        return a + b
