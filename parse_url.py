import requests
from retrying import retry

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}


# 可以尝试3次
@retry(stop_max_attempt_number=3)
def _parse_url(url):
    resp = requests.get("http://www.baidu.com", headers=headers, timeout=3, verify=False)
    assert resp.status_code == 200
    return resp.content.decode()


def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str