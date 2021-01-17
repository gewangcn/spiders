from selenium import webdriver
import time

# 实例化一个浏览器
driver = webdriver.Chrome()
# 发送请求
driver.get("http://www.baidu.com")
# 元素定位的方法
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
driver.find_elements_by_class_name("bn-submit").click()
driver.find_elements_by_id("captcha_image").get_attribute()
# 无界面模式
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
# 设置窗口大小
driver.set_window_size(1920,1080)
# 最大化窗口
#driver.maximize_window()
driver.get("http://www.sina.com.cn")
driver.save_screenshot('./sina.png')


ret1 = driver.find_elements_by_xpath("//ul[@id='detail-list']/li")
for li in ret1:
    li_text = li.find_element_by_xpath(".//h1/p").text
    li_attr = li.find_element_by_xpath(".//a[@class='share_url']").get_attribute("href")








# 获取html字符串  浏览器elements
driver.page_source
# 当前的url
print(driver.current_url)
# 获取cookie
cookies = driver.get_cookies()
cookie_dict = {i["name"]: i["value"] for i in cookies}
print(cookie_dict)
time.sleep(6)
# 退出浏览器
driver.quit()
# 退出当前页码
driver.close()
