import requests
from bs4 import BeautifulSoup as BS
import json


def movie_Crawling(html):
    temp_list = []
    temp_dict = {}

    target = html.find(class_="_content")
    list = target.find_all('li')
    no = 0
    for n in range(0, len(list)):
        if no == 9:
            break
        print("=================================")
        print("No.", no+1)
        no += 1
        # 영화 제목
        title = list[n].find(class_="movie_info").find("strong").text
        print("제목 :\t", title)
        # 개봉
        release = list[n].find(class_="movie_item").find("dd").text
        print("개봉 :\t", release)
        # 일간
        eachDay = list[n].find("dl").find_all("dd")[1].text
        print("일간 :\t", eachDay)
        # 누적
        ppData = list[n].find("dl").find_all("dd")[2].text
        print("누적 :\t", ppData)
        temp_list.append([no,title,release,eachDay,ppData])
        temp_dict[str(no)] = {'title': title, 'release': release, 'Today': eachDay, 'accumulate': ppData}

    return temp_list, temp_dict
#====================================================================================================
def toJson(rank_dict):
    with open('movie_ranking.json', 'w', encoding='utf-8') as file:
        json.dump(rank_dict, file, ensure_ascii=False, indent='\t')
#====================================================================================================
rank_list = []
rank_dict = {}

req = requests.get('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4')
html = BS(req.text, 'html.parser')

rank_temp = movie_Crawling(html)
rank_list += rank_temp[0]
rank_dict = dict(rank_dict, **rank_temp[1])

# 리스트 출력
for item in rank_list:
    print(item)

# 사전형 출력
#for item in rank_dict:
#    print(item, rank_dict[item]['title'], rank_dict[item]['release'])


# Json파일 생성
toJson(rank_dict)

