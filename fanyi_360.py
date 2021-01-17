import requests
import json
import sys

query_string = sys.argv[1]
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
           "Accept": "application/json, text/plain, */*",
           "Cookie": "QiHooGUID=7BF45D954FBC3FFFDBA99C389E861DBB.1608716611603; __guid=144965027.2917255130271688700.1608716612151.111; count=1; __huid=11oenkFLzG3AhAQCqFob%2Bth83pIOw%2Brdw%2B55mo%2BQAYQrg%3D; gtHuid=1",
           "pro": "fanyi",
           "Origin": "http://fanyi.so.com"
           }

data = {
    "eng": 0,
    "validate": "",
    "ignore_trans": 0,
    "query": query_string
}

post_url = "http://fanyi.so.com/index/search"

resp = requests.post(post_url, data=data, headers=headers)
dict_ret= json.loads(resp.content.decode())
ret = dict_ret["data"]["fanyi"]
print(ret)
