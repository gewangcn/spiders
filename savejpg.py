import requests

resp = requests.get("https://edu-tob.bdimg.com/v1/pc/pc%E5%85%88%E9%A6%96%E9%A1%B5%E5%A4%B4%E5%9B%BE5120-640-1608686903810.png")
with open("a.png", "wb") as f:
    f.write(resp.content)
# 返回cookie信息转换的字典 键值对
se = requests.session()