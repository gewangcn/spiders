from selenium import webdriver
import time

class DouyuSpider:
    def __init__(self):
        self.temp_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath('//ul[@class="layout-Cover-list"]/li')
        print(li_list)
        content_list = []
        for li in li_list:
            items = dict()
            items["title"] = li.find_element_by_xpath('.//h3[@class="DyListCover-intro"]').get_attribute("title")
            items["username"] = li.find_element_by_xpath('.//div[contains(@class,"DyListCover-userName")]').text
            items["hot"] = li.find_element_by_xpath('.//span[@class="DyListCover-hot is-template"]').text
            print(items)
            content_list.append(items)
        next_url_list = self.driver.find_elements_by_xpath(
            '//ul[@class="dy-Pagination ListPagination"]/li[@aria-disabled="false"]')
        return content_list, next_url_list[0] if len(next_url_list) > 0 else None

    def save_content(self, content_list):
        pass

    def run(self):
        # start_url
        # 发送请求
        self.driver.get(self.temp_url)
        print(self.driver.page_source)
        with open("./douyu.html", "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        # 获取数据
        content_list, next_url = self.get_content_list()
        # 保存数据
        self.save_content(content_list)
        # 循环
        while next_url is not None:
            self.driver.get(self.next_url)
            content_list, next_url = self.get_content_list()
            self.save_content(content_list)
            next_url.click()
            time.sleep(3)
        self.driver.quit()


if __name__ == "__main__":
    du = DouyuSpider()
    du.run()
