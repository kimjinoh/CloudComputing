import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4%20%ED%9D%A5%ED%96%89%EC%88%9C%EC%9C%84'
res = urllib.request.urlopen(url).read()
movie = BeautifulSoup(res, 'html.parser')

movie = movie.findAll("div", class_="thumb")
print(movie)
count = 0
for ul in movie:
    count += 1
    imgUrl = ul.find("img")["src"]
    urllib.request.urlretrieve(imgUrl,"C:/Users/LG/Desktop/CloudCom/page/projectPage/poster/"+"%d" % count + '.jpg')
    if count == 8:
        break