import requests
from bs4 import BeautifulSoup

url = "https://www.avito.ru/"

me = {
   "authority":"www.avito.ru",
"method":"GET",
"path":"/",
"scheme":"https",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
"Cache-Control":"max-age=0",
"Cookie":"""gMltIuegZN2COuSe=EOFGWsm50bhh17prLqaIgdir1V0kgrvN; u=32bbc8s9.1hr2xb0.l78q8bpljlw0; v=1706656769; buyer_laas_location=621540; luri=all; buyer_location_id=621540; dfp_group=26; abp=1; _ym_uid=166054555748791871; _ym_d=1706656773; _ym_isad=1; _gcl_au=1.1.407113714.1706656773; yandex_monthly_cookie=true; _ym_visorc=b; _ga=GA1.1.381982320.1706656774; tmr_lvid=70ff9dcb3e438490da6eaaf293fce3c4; tmr_lvidTS=1660545557010; f=5.cc913c231fb04ceddc134d8a1938bf88a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa1a2a574992f83a9246b8ae4e81acb9fa46b8ae4e81acb9fae992ad2cc54b8aa8af305aadb1df8cebc93bf74210ee38d940e3fb81381f359178ba5f931b08c66aff38e8d292af81e50df103df0c26013a2ebf3cb6fd35a0ac71e7cb57bbcb8e0ff0c77052689da50ddc5322845a0cba1aba0ac8037e2b74f92da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eabdc5322845a0cba1a0df103df0c26013a037e1fbb3ea05095de87ad3b397f946b4c41e97fe93686ad38bc41f144dd3bd2980ebe1621c8ebff02c730c0109b9fbb28d48df890030ee0d3322f0425f519880e28148569569b7923569110cbefb342e19d3cabfc0245fb2ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3aefcfb0a8b1110195621e08b64f8348743de19da9ed218fe23de19da9ed218fe2ddb881eef125a8703b2a42e40573ac3c9ca703028dd55cfb3882be5d35524c6c; ft="sR24f1LYXupB3zRqVuzZk/cUvyYGfOY5A/VVkB0F7jV/rqhP00d41/bsdCcs1cyavn6Nn++nIgdoVw08VUeYjEWXsHuu7LrZRdbv3vYVQ4qjyH5xcIe4kbgQavn/HCFOJ68Bqro3d1KUpYSG93dSFjSe7WgAprBNR990nGcMuHiNPSkX2+j70PrdvMkyhMHp"; srv_id=3lQ9YTBxRYL-ytP-.JI2Rq7ZiedbYdRZgCNZm3sq7oJ_XWe9L41ErvDWli3WUy6w75EAI2sep5CBd5XkXA2rP.lAmoeDeHL_BSqmxRLfBYPvL-mEXCVxHVUPewEt5NVVQ=.web; sx=H4sIAAAAAAAC%2FwTAQQ7CIBAF0Lv8tQtw4I%2FDcWQgjTWQxtiFDXf3XSDJ6sputMxEa%2FpsYq451KpuKBdOFMz5e7zeMW9yDJ%2Bhn7uNr49ji%2Fv90yNuaChRAzWJJFnrHwAA%2F%2F9UlQewWwAAAA%3D%3D; _ga_M29JC28873=GS1.1.1706656774.1.1.1706656943.60.0.0; tmr_detect=0%7C1706656946368""",
"If-None-Match":"""W/"15ea86-VgWgR3CtRG1HiTN9zlk8ubH3IWA""",
"Referer":"https://www.google.com/",
"Sec-Ch-Ua":""""Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121""""",
"Sec-Ch-Ua-Mobile":"?0",
"Sec-Ch-Ua-Platform":"macOS",
"Sec-Fetch-Dest":"document",
"Sec-Fetch-Mode":"navigate",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-User":"?1",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}


r = requests.get(url=url, headers=me)

src = r.text

with open("html/avito_website.html", "w", encoding="utf-8") as file:
    file.write(src)

# def take_for_sort_box():
#
#     return