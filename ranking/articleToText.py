#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup
from threading import Thread
from time import sleep


def article_crw():
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

#=================================================


def total():
    while True:
        article_crw()
        sleep(85000)
#================================================




def main():
    th = Thread(target=total)
    th.demon = True
    th.start()


if __name__ == '__main__':
    main()
