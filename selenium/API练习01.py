# coding = utf-8
from selenium import webdriver
import time

browser = webdriver.Chrome() # 获得Google的驱动
time.sleep(3)
browser.get("http://www.baidu.com")
# 浏览器- 开发者工具 - 右击检查，可查看相应元素的 id 等
#通过 id 定位到 input 输入框，然后输入待搜索内容：CSDN
# browser.find_element_by_id("kw").send_keys("CSDN")
#搜索的按钮的 id 叫做 su ，我需要点一下按钮 click()
# browser.find_element_by_id("su").click()

# 通过name定位
'''
browser.find_element_by_name("wd").send_keys("网易云音乐")
browser.find_element_by_id("su").click()'''

# 通过链接内容定位
'''
browser.find_element_by_link_text("高考加油").click()
browser.find_element_by_partial_link_text("高考").click()'''

#通过tag name 方式定位， 不能成功，因为input太多了不唯一。
'''browser.find_element_by_tag_name("input").send_keys("selenium")'''

# CSS 定位,id --> #id名,class唯一时 --> .class名
'''
browser.find_element_by_css_selector("#kw").send_keys("hello")
browser.find_element_by_css_selector(".s_ipt").send_keys("hello")
'''
# XPath定位，* 表示将前面的内容全部省略掉，用 id 定位
'''
#browser.find_element_by_xpath("//*[@id='kw']").send_keys("521")
browser.find_element_by_xpath("//*[@name='wd']").send_keys("521")
browser.find_element_by_xpath("//*[@id='su']").click()
'''

# 现在文本框输入 “CSDN"，再清楚内容，再次输入”元龙“进行搜索
'''
browser.find_element_by_id("kw").send_keys("CSDN")
time.sleep(2)#等待两秒钟，否则代码执行太快看不到结果，也避免因为其他原因导致浏览器未进行该操作
browser.find_element_by_id("kw").clear()
time.sleep(2)
browser.find_element_by_id("kw").send_keys("元龙")
# browser.find_element_by_id("su").click()
browser.find_element_by_id("su").submit()
'''

# 获取元素文本
# print(browser.find_element_by_id("s-bottom-layer-right").text)

# 智能等待
'''
browser.find_element_by_id("kw").send_keys("乃万")
browser.find_element_by_id("su").click()
browser.implicitly_wait(10)
browser.find_element_by_link_text("乃万_百度百科").click()'''

time.sleep(3)
#quit不仅关闭窗口还会彻底退出webdriver，释放连接。close只是关闭窗口。
browser.quit()