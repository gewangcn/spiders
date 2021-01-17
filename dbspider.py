import requests
import json


class DoubanSpider:
    def __init__(self):
        self.url_temp = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_variety_show/items?start={}&count=8&loc_id=108288"
        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15\
         (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
                        "Referer": "https://m.douban.com/tv/"}

    def parse_url(self, url):
        resp = requests.get(url, headers=self.headers)
        return resp.content.decode()

    def get_content_list(self, json_str):
        ret_dict = json.loads(json_str)
        content_list = ret_dict["subject_collection_items"]
        total = ret_dict["total"]
        return content_list, total

    def save_content_list(self, content_list):
        with open("douban.json", "a", encoding="utf-8") as f:
            for cont in content_list:
                f.write(json.dumps(cont, ensure_ascii=False))
                f.write("\n")

    def run(self):
        num = 0
        total = 50
        while num < total:
            # start_url
            url = self.url_temp.format(num)
            # 发送请求
            json_str = self.parse_url(url)
            # 提取数据
            content_list, total = self.get_content_list(json_str)
            # 保存数据
            self.save_content_list(content_list)
            num += 8


if __name__ == "__main__":
    dbs = DoubanSpider()
    dbs.run()
