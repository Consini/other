from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
driver = webdriver.Chrome()
driver.maximize_window()
# 定位一组元素，get_attribute：获得属性值
'''
file_path = 'file:///' + os.path.abspath('html\\checkbox.html')
driver.get(file_path)
driver.maximize_window()
# 选择页面上所有的input，然后从中过滤出所有的 checkbox 并勾选之
inputs = driver.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
'''
# 多层窗口定位:通过switch_to_frame() 方法来进行定位
'''
file_path = 'file:///' + os.path.abspath('html\\frame.html')
driver.get(file_path)
driver.implicitly_wait(30)
#从默认页面跳转到 ifrome1（id = f1）
driver.switch_to.frame("f1")
#再找到其下面的 ifrome2 (id = f2)
driver.switch_to.frame("f2")
#下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(2)
# 跳转到默认页面
driver.switch_to.default_content()
driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()
'''
# 层级定位
'''
file_path = 'file:///' + os.path.abspath('html\\level_locate.html')
driver.get(file_path)
#点击Link1链接（弹出下拉列表）
driver.find_element_by_link_text('Link1').click()
driver.implicitly_wait(10)
#方法 1：通过文本链接Action定位
action = driver.find_element_by_link_text('Action')
driver.implicitly_wait(10)
webdriver.ActionChains(driver).move_to_element(action).perform()

#方法 2： 找到id 为dropdown1的父元素
# WebDriverWait(driver,10).until(lambda the_driver:
# the_driver.find_element_by_id('dropdown1').is_displayed())
# #在父亲元件下找到link 为Action 的子元素
# menu = driver.find_element_by_id('dropdown1').find_element_by_link_text('Action')
# #鼠标定位到子元素上
# webdriver.ActionChains(driver).move_to_element(menu).perform()
'''
#下拉框处理
'''
file_path = 'file:///' + os.path.abspath('html\\drop_down.html')
driver.get(file_path)
# 方法1：xpath 定位
driver.find_element_by_xpath("//*[@id='ShippingMethod']/option[3]").click()
# 方法2： 先定位一组元素
lists = driver.find_elements_by_tag_name("option")
for list in lists:#遍历寻找自己想要的
    if list.get_attribute('value') == '10.69':
        list.click()
lists[2].click() # 通过下标定位
'''
# alert 框处理：switch_to.alert
# text 返回alert/confirm/prompt 中的文字信息
# accept 点击确认按钮
# dismiss 点击取消按钮，如果有的话
'''
file_path = 'file:///' + os.path.abspath('html\\alert.html')
driver.get(file_path)
driver.find_element_by_id("tooltip").click()# 在这个例子中 id,link text 都可以用来定位
time.sleep(1)
alert = driver.switch_to.alert
time.sleep(1)
print("alert text:"+alert.text)
alert.accept()
'''
# send_keys 输入值，这个alert\confirm 没有对话框就不能用了，不然会报错
'''
file_path = 'file:///' + os.path.abspath('html\\send.html')
driver.get(file_path)
#driver.find_element_by_xpath("/html/body/input").click()
driver.find_element_by_tag_name("input").click()
alert = driver.switch_to.alert
alert.send_keys("少卿大人")
alert.accept()
'''
# div 模块的处理
'''
file_path = 'file:///' + os.path.abspath('html\\modal.html')
driver.get(file_path)
time.sleep(3)
driver.find_element_by_id("show_modal").click()
time.sleep(1)

ddiv = driver.find_element_by_class_name("modal-body")
ddiv.find_element_by_id("click").click()
#ddiv.find_element_by_partial_link_text("click").click()
time.sleep(1)

#button = driver.find_element_by_class_name("modal-footer").find_elements_by_tag_name("button")
buttons = driver.find_elements_by_tag_name("button")
buttons[0].click()
'''
# 上传文件操作

file_path = 'file:///' + os.path.abspath('html\\upload.html')
driver.get(file_path)
driver.find_element_by_name("file").send_keys("D:\\Program Files\\python\\project\\selenium\\html\\upload.html")

time.sleep(2)
driver.quit()