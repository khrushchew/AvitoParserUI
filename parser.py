import requests
from bs4 import BeautifulSoup

# url = "https://www.looperman.com/acapellas"
# me = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
# }
# r = requests.get(url=url, headers=me)
# src = r.text

# with open("html/looperman_website.html", "w", encoding="utf-8") as file:
#     file.write(src)

with open("html/looperman_website.html", "r", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

sort_items = soup.find_all("fieldset")

sort_dict = {i.find("label").text: [j.text for j in i.find_all("option")] for i in sort_items}
