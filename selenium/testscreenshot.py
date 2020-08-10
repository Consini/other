# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import os
class Baidu1(unittest.TestCase):
   #test fixture，初始化环境
   def setUp(self):
       self.driver = webdriver.Firefox()
       self.driver.implicitly_wait(30)
       self.base_url = "http://www.baidu.com/"
       self.verificationErrors = []
       self.accept_next_alert = True

       # 测试用例，必须以test开头
   def test_hao(self):
       driver = self.driver
       driver.get(self.base_url + "/")
       driver.find_element_by_link_text("hao123").click()
       time.sleep(2)
       # 异常捕获，出现错误进行错误截图，
       try:
           self.assertEqual(u'hao_上网从这里开始', driver.title)
       except:
           self.savescreenshot(driver, 'hao.png')

    # 判断element是否存在，可删除
   def is_element_present(self, how, what):
       try:
           self.driver.find_element(by=how, value=what)
       except NoSuchElementException as e: return False
       return True

       # 判断alert是否存在，可删除
   def is_alert_present(self):
       try:
           self.driver.switch_to_alert()
       except NoAlertPresentException as e:
           return False
       return True

       # 关闭alert，可删除
   def close_alert_and_get_its_text(self):
       try:
           alert = self.driver.switch_to_alert()
           alert_text = alert.text
           if self.accept_next_alert:
               alert.accept()
           else:
               alert.dismiss()
           return alert_text
       finally: self.accept_next_alert = True

       # test fixture，清除环境
   def tearDown(self):
       self.driver.quit()
       self.assertEqual([], self.verificationErrors)
   def savescreenshot(self, driver, file_name):
       if not os.path.exists('./errorImage'):
           os.makedirs('./errorImage')
       now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
       # 截图保存
       driver.get_screenshot_as_file('./errorImage/' + now + '-' + file_name)
       time.sleep(1)
if __name__ == "__main__":
    # 执行用例
    unittest.main()
'''
可以增加verbosity参数，例如unittest.main(verbosity=2)
在主函数中，直接调用main() ，在main中加入verbosity=2 ，这样测试的结果就会显示的更加详细。
这里的verbosity 是一个选项, 表示测试结果的信息复杂度，有三个值:
0 ( 静默模式): 你只能获得总的测试用例数和总的结果比如总共100个失败,20 成功80
1 ( 默认模式): 非常类似静默模式只是在每个成功的用例前面有个“ . ” 每个失败的用例前面有个“F”
2 ( 详细模式): 测试结果会显示每个测试用例的所有相关的信息
'''