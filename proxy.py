import requests

# proxies = {"http": "http://113.214.13.1:1080"}
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
#  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
#
# resp = requests.get("http://www.baidu.com", proxies=proxies, headers=headers)
# print(resp.status_code)
# print(resp.content.decode())

cookies = "BIDUPSID=27E9DE2A975BB5BC9C7029C5D1C0A7B9; \
BDORZ=FFFB88E999055A3F8A630C64834BD6D0; PSTM=1608772408; \
BAIDUID=47D52796596E90A3BC16B68BE3467B4F:FG=1; \
AIDUID_BFESS=47D52796596E90A3175233C4FEB86998:FG=1; \
BDRCVFR[1kRcOFa5hin]=mk3SLVN4HKm; H_PS_PSSID=; delPer=0; \
PSINO=1; BA_HECTOR=a02k2l8gak802400e31fu7tid0r"
requests.get("url", headers="", cookies="")
c_dict = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
print(c_dict)
