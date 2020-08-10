from selenium import webdriver
from selenium.webdriver.common.keys import Keys #需要引入keys 包
from selenium.webdriver.common.action_chains import ActionChains

import time,os
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#打印标题和 URL
'''
print(driver.title) #百度一下，你就知道
print(driver.current_url) #http://www.baidu.com
'''

# driver.find_element_by_id("kw").send_keys("天官赐福")
# driver.find_element_by_id("su").click()

# driver.implicitly_wait(10)
# driver.find_element_by_partial_link_text("天官赐福").click()
# time.sleep(2)

driver.maximize_window()# 浏览器最大化与缩小
#driver.minimize_window()# 浏览器缩小

# time.sleep(2)
# driver.set_window_size(400,600)# 浏览器设置固定大小
# time.sleep(2)

#浏览器的前进和后退
'''
driver.back()
time.sleep(2)
driver.forward()
'''

#浏览器滚动条操作,用的是 js
'''
js = "var q=document.documentElement.scrollTop=10000" #滚动条拖到最底端
driver.execute_script(js)
time.sleep(2)
js = "var q=document.documentElement.scrollTop=0" #滚动条拖到最顶端
driver.execute_script(js)
#windows.scollTo(x-coord,y-coord),x-coord 是文档中的横轴坐标,y-coord 是文档中的纵轴坐标。控制浏览器的上下左右
driver.execute_script("window.scrollTo(1000,0)") #滚动条拖到最右端
time.sleep(2)
driver.execute_script("window.scrollTo(0,1000)") #滚动条拖到最左端
'''

# TAB键和 Inter 键的用法
'''
driver.get("http://127.0.0.1:81/biz/user-login.html")
driver.implicitly_wait(10)
driver.maximize_window() # 浏览器全屏显示
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_id("account").send_keys(Keys.TAB)
time.sleep(2)
#tab 的定位相当于清除了密码框的默认提示信息，等同上面的clear()
#通过定位密码框，enter（回车）来代替登陆按钮
driver.find_element_by_name("password").send_keys("Kou0702.")
#也可定位登陆按钮，通过enter（回车）代替click()
driver.find_element_by_id("login").send_keys(Keys.ENTER)
'''

# 组合键用法：先输入天官赐福进行搜索，然后把输入框内容全选剪切后再次输入雾山五行进行搜索
'''
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a') #全选
time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x') #剪切
time.sleep(2)
driver.find_element_by_id("kw").send_keys("雾山五行")
driver.find_element_by_id("su").click()
'''

#鼠标事件
'''
driver.find_element_by_id("kw").send_keys("天官赐福")
su1 = driver.find_element_by_id("su")
ActionChains(driver).context_click(su1).perform() #右键
ActionChains(driver).double_click(su1).perform() #双击
'''


time.sleep(2)
driver.quit()