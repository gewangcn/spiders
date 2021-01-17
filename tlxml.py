import requests
from lxml import etree
import threading
from queue import Queue


class QiubaiSpdier:
    def __init__(self):
        self.url_temp = "http://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {"User-Agent": ""}
        self.url_queue = Queue()
        self.html_str_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        for i in range(1, 14):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self):
        while True:
            url = self.url_queue.get()
            resp = requests.get(url, headers=self.headers)
            self.html_str_queue.put(resp.content.decode())
            self.url_queue.task_done()

    def get_content_list(self):
        while True:
            html_str = self.html_str_queue.get()
            html = etree.HTML(html_str)
            div_list = html.xpath("//div[@id='content-left']/div")
            content_list = []
            for div in div_list:
                item = {}
                or_content = div.xpath(".//div[@class='content']/span/text()")
                item["content"] = [i.replace("\n", "") for i in or_content]
                content_list.append(item)
            self.content_queue.put(content_list)
            self.html_str_queue.task_done()

    def save_content_list(self):
        while True:
            content_list = self.content_queue.get()
            for i in content_list:
                pass  # '保存数据'
            self.content_queue.task_done()

    def run(self):
        thread_list = []
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        # 发送请求慢 开启三个线程做
        for i in range(3):
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)
        t_html = threading.Thread(target=self.get_content_list)
        thread_list.append( t_html)
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)
        for t in thread_list:
            t.setDaemon(True)  # 设为守护线程  主线程结束 主线程结束
            t.start()
        for q in [self.url_queue, self.html_str_queue, self.content_queue]:
            q.join()  # 主线阻塞 等待子线程执行完成
        print("主线程结束")