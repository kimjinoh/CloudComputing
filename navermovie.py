import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/running/current.nhn'
res = urllib.request.urlopen(url).read()
movie = BeautifulSoup(res, 'html.parser')

movie = movie.findAll("div", class_="thumb")
print(movie)
out = open("movieimgs.html", 'w')
count = 0
for ul in movie:
    count += 1
    imgUrl = ul.find("img")["src"]
    urllib.request.urlretrieve(imgUrl, "%d" % count + '.jpg')
    print(ul.img, file=out)