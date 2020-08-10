# -*- coding: utf-8 -*-
import unittest,csv
import os,sys
import time
#手工添加案例到套件
'''
discover 是通过递归的方式到其子目录中从指定的目录开始， 找到所有测试模块并返回一个包含它们对象的
TestSuite ，然后进行加载与模式匹配唯一的测试文件，discover 参数分别为
discover(dir,pattern,top_level_dir=None)'''
def createsuite():
    discover = unittest.defaultTestLoader.discover('../selenium', pattern='test*.py', top_level_dir=None)
    print(discover)
    '''测试套件<unittest.suite.TestSuite tests=[<unittest.suite.TestSuite tests=[<unittest.suite.TestSuite 
    tests=[<testbaidu1.Baidu1 testMethod=test_baidusearch>, <testbaidu1.Baidu1 testMethod=test_hao>]>]>, 
    <unittest.suite.TestSuite 
    tests=[<unittest.suite.TestSuite tests=[<testbaidu2.Baidu2 testMethod=test_baidusearch>]>]>]>'''
    return discover

if __name__=="__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)