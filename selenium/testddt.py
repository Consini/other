#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
import os,sys,csv
from ddt import ddt, data, unpack ,file_data
def getCsv(file_name):
    rows = []
    path = sys.path[0]
    print(path)
    with open(path+'/data/'+file_name,'rt',encoding='UTF-8') as f:
        readers = csv.reader(f, delimiter=',', quotechar='|')
        next(readers, None)
        for row in readers:
            temprows = []
            for i in row:
                temprows.append(i)
            rows.append(temprows)
        return rows

#引入ddt
@ddt
class testddt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
#测试用例，必须以test开头,增加ddt数据

    # 单变更时不使用unpack
    @data("王凯", "Lisa", "天官赐福")
    @unittest.skip("skipping")
    def test_hao1(self, value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    # @data([3, 2], [4, 3], [5, 3])
    @data(["Lsia",u"Lsia_百度搜索"],[u"双笙",u"双笙_百度搜索"],[u"999",u"999_百度搜索"])
    @unpack
    @unittest.skip("skipping")
    def test_hao2(self,value,expected_value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertEqual(expected_value, driver.title)#判断搜索网页的title和期望的是否一致
        print(expected_value)#打印期待值
        print(driver.title)


    @data(*getCsv('test_baidu_data.txt'))
    @unpack
    @unittest.skip("skipping")
    def test_hao(self, value, expected_value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertEqual(expected_value, driver.title)  # 判断搜索网页的title和期望的是否一致
        print(expected_value)  # 打印期待值
        print(driver.title)

    # 使用file_data需要在cmd窗口下运行，否则找不到文件
    @file_data('json/test_data_list.json')
    @unpack
    def test_hao(self, value):
            driver = self.driver
            driver.get(self.base_url + "/")
            driver.find_element_by_id("kw").clear()
            driver.find_element_by_id("kw").send_keys(value)
            driver.find_element_by_id("su").click()
            time.sleep(2)

#判断element是否存在，可删除
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
#判断alert是否存在，可删除
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException as e:
            return False
        return True
#关闭alert，可删除
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

#test fixture，清除环境
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

#错误截图
    def savescreenshot(self,driver,file_name):
        if not os.path.exists('./errorImage'):
            os.makedirs('./errorImage')
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        # 截图保存
        driver.get_screenshot_as_file('./errorImage/' + now + '-' + file_name)
        time.sleep(1)

if __name__ == "__main__":
#执行用例
   unittest.main()

'''
可以增加verbosity参数，例如unittest.main(verbosity=2)在主函数中，直接调用main() ，在main中加入verbosity=2 ，这样测试的结果就会显示的更加详细。
这里的verbosity 是一个选项, 表示测试结果的信息复杂度，有三个值:
0 ( 静默模式): 你只能获得总的测试用例数和总的结果比如总共100个失败,20 成功80
1 ( 默认模式): 非常类似静默模式只是在每个成功的用例前面有个“ . ” 每个失败的用例前面有个“F”
2 ( 详细模式): 测试结果会显示每个测试用例的所有相关的信息
'''
