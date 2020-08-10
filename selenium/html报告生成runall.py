# -*- coding: utf-8 -*-
import unittest
import os,sys
import time
import HTMLTestRunner
#手工添加案例到套件，
def createsuite():
    discover=unittest.defaultTestLoader.discover('../selenium',pattern='testba*.py',top_level_dir=None)
    print(discover)
    return discover
if __name__=="__main__":
    # #sys.path 是python的搜索模块的路径集，返回结果是一个list
    # curpath=sys.path[0]
    #
    # print(sys.path)
    # print("************")
    # print(sys.path[0])
    #
    # #取当前时间
    # '''
    # strftime作用是格式化时间戳为本地时间
    # time()函数用于返回当前时间的时间戳（1970年01月08时00分00秒到现在的浮点秒数）
    # localtime()函数作用是格式化时间戳为本地 struct_time
    # '''
    # if not os.path.exists(curpath+'/resultreport'):
    #     os.makedirs(curpath+'/resultreport')

    # ./ 表示当前目录
    if not os.path.exists('./resultreport'):
        os.mkdir('./resultreport')

    now=time.strftime("%Y-%m-%d-%H %M %S",time.localtime(time.time()))

    print("-----------")
    print(time.time())
    print("-----------")
    print(time.localtime(time.time()))
    print("-----------")
    print(now)


    # filename = curpath + '/resultreport/' + now + 'resultreport.html'
    filename = './resultreport/' + now + 'resultreport.html'
    with open(filename, 'wb') as fp:
        # 出html报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况', verbosity=2)
        suite = createsuite()
        runner.run(suite)