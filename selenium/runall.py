# -*- coding: utf-8 -*-
import unittest,csv
import os,sys
import time
#导入testbaidu1，testbaidu2
import testbaidu1
import testbaidu2
#手工添加案例到套件，
def createsuite():
    suite = unittest.TestSuite()

    # 将某个类的某个测试用例加入到测试容器（套件）中
    # suite.addTest(testbaidu1.Baidu1("test_baidusearch"))
    # suite.addTest(testbaidu1.Baidu1("test_hao"))
    # suite.addTest(testbaidu2.Baidu2("test_baidusearch"))

    # 把一个类里面的所有测试方法添加到套件里面，makeSuite可以实现把测试用例类内所有的测试case组成的测试套
    # 件TestSuite ，unittest 调用makeSuite的时候，只需要把测试类名称传入即可
    # suite.addTest(unittest.makeSuite(testbaidu1.Baidu1))
    # suite.addTest(unittest.makeSuite(testbaidu2.Baidu2))

    # 把一个类里面的所有测试方法添加到套件里面，TestLoader 用于创建类和模块的测试套件
    suite1 = unittest.TestLoader().loadTestsFromTestCase(testbaidu1.Baidu1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(testbaidu2.Baidu2)
    suite = unittest.TestSuite([suite1, suite2])
    return suite

if __name__=="__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)