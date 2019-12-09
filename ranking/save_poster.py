import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from threading import Thread
from time import sleep


def save_poster():
    while True:
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4%20%ED%9D%A5%ED%96%89%EC%88%9C%EC%9C%84'
        res = urllib.request.urlopen(url).read()
        movie = BeautifulSoup(res, 'html.parser')

        movie = movie.findAll("div", class_="thumb")
        print(movie)
        count = 0
        for ul in movie:
            count += 1
            imgUrl = ul.find("img")["src"]
            urllib.request.urlretrieve(imgUrl,"./projectPage/poster/"+"%d" % count + '.jpg')
            if count == 8:
                break
    sleep(86400)



def main():
    th = Thread(target=save_poster)
    th.demon = True
    th.start()


if __name__ == '__main__':
    main()