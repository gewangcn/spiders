import requests
import re
import json


class Neihan:
    def __init__(self):
        self.temp_url = "https://www.haha.mx/topic/13648/new/{}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

    def parse_url(self, url):
        resp = requests.get(url, headers=self.headers)
        return resp.content.decode()

    def get_first_page_content_list(self, html_str):
        content_list = re.findall(r"<p class=\"word-wrap joke-main-content-text\">(.*?)</p>", html_str, re.S)
        return content_list

    def save_content_list(self,content_list):
        with open("neihan.txt", "a", encoding="utf-8") as f:
            for cont in content_list:
                f.write(json.dumps(cont, ensure_ascii=False))
        print("保存成功")

    def run(self):
        num = 1
        # start_url
        url = self.temp_url.format(num)
        # 发送请求
        html_str = self.parse_url(url)
        # 提取数据
        contetn_list = self.get_first_page_content_list(html_str)
        # 保存
        self.save_content_list(contetn_list)
        has_more = True
        max_time = 0.002
        while has_more:
            next_url = self.temp_url.format(max_time)
            json_str = self.parse_url(next_url)
            content_list, max_time, has_more = self.get_content_list(json_str)
            self.save_content_list(content_list)

if __name__ == "__main__":
    nh = Neihan()
    nh.run()
