import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=03,205&theatercode=0228&date=20191126'
res = urllib.request.urlopen(url).read()
movie = BeautifulSoup(res, 'html.parser')

movie = movie.findAll("div", class_="col-times")

#print(movie)

out=open("01_outputs.html",'w', -1, "utf-8")

for ul in movie:
    print(ul, file=out)

