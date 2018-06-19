# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# 初始化,声明浏览器
# browser = webdriver.Firefox()
browser = webdriver.Chrome()

try:
    # 访问页面
    browser.get("https://baidu.com")

    # 提取 搜索框 节点，
    input_text = browser.find_element_by_id('kw')

    # 节点交互，Selenium驱动浏览器执行某些操作，
    input_text.send_keys('Python')

    # 模拟键盘Enter键提交搜索需求
    input_text.send_keys(Keys.ENTER)

    # 显示等待
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)

    # 获取cookies
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()

