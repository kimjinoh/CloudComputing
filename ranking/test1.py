import urllib.request
from bs4 import BeautifulSoup
import sys

url = "https://entertain.naver.com/movie"
html = urllib.request.urlopen(url)

bsObj = BeautifulSoup(html, "html.parser")

div = bsObj.find("div", {"id": "content"})
ul = div.find("ul", {"class": "news_lst"})
lis = ul.findAll("li")
out = open('output.txt', 'w')

for li in lis:
    p_tag = li.find("a", {"class": "tit"})
    print(p_tag.text, file=out)