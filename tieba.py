import requests


class TiebaSpider:
    def __init__(self, tbname):
        # https://tieba.baidu.com/f?ie=utf-8&kw=李毅fr=search
        self.tbname = tbname
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tbname + "&ie=utf-8&pn={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

    def get_url_list(self):
        '''构造url列表'''
        url_list = []
        for i in range(3):
            url_list.append(self.url_temp.format(i * 50))
        return url_list

    def parse_url(self, url):
        '''发送请求'''
        print(url)
        resp = requests.get(url, headers=self.headers)
        return resp.content.decode()

    def save_html(self, html_str, page_num):
        '''保存html'''
        file_path = "{}-第{}页.html".format(self.tbname, page_num)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        # 遍历发送时请求
        url_list = self.get_url_list()
        for url in url_list:
            html_str = self.parse_url(url)
            page_num = url_list.index(url) + 1
            # 保存数据
            self.save_html(html_str, page_num)


if __name__ == "__main__":
    tb = TiebaSpider("nba")
    tb.run()
