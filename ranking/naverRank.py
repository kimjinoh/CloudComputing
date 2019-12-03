# import
from bs4 import BeautifulSoup
from urllib.request import urlopen
from threading import Thread
from time import sleep


def printHello():
    while True:
        url = urlopen(
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4%20%ED%9D%A5%ED%96%89%EC%88%9C%EC%9C%84")
        bs = BeautifulSoup(url, 'html.parser')
        body = bs.body

        target = body.find(class_="_content")
        list = target.find_all('li')
        no = 1
        for n in range(0, len(list)):
            if no == 9:
                break
            print("=================================")
            print("No.", no)
            no += 1
            # 영화 제목
            title = list[n].find(class_="movie_info").find("strong").text
            print("제목 :\t", title)

            # 개봉
            try:
                openDay = list[n].find(class_="movie_item").find("dd").text
                print("개봉 :\t", openDay)
            except IndexError:
                print("개봉 :\t 정보 없음")

                # 일간
            try:
                everyDay = list[n].find("dl").find_all("dd")[1].text
                print("일간 :\t", everyDay)
            except IndexError:
                print("일간 :\t 정보 없음")

                # 누적
            try:
                ppData = list[n].find("dl").find_all("dd")[2].text
                print("누적 :\t", ppData)
            except IndexError:
                print("누적 :\t 정보 없음")

        sleep(86400)


def main():
    th = Thread(target=printHello)
    th.demon = True
    th.start()


if __name__ == '__main__':
    main()