# import
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = urlopen("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4%20%ED%9D%A5%ED%96%89%EC%88%9C%EC%9C%84")
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
    print("영화 제목 :\t", title)

    # 개봉
    try:
        openDay = list[n].find(class_="movie_info").find_all("dl")[1].find("dd")
        openDayList = [openDay.text.strip() for openDay in openDay]
        print("개봉 :\t", openDayList)
    except IndexError:
        print("개봉 :\t 정보 없음")
    # 일간
    try:
        everyDay = list[n].find(class_="movie_info").find_all("dl")[1].find("dd")
        everyDayList = [everyDay.text.strip() for everyDay in everyDay]
        print("일간 :\t", everyDayList)
    except IndexError:
        print("일간 :\t 정보 없음")
