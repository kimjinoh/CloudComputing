import datetime
import re
import urllib.request
from datetime import datetime, timedelta, time
import time

from bs4 import BeautifulSoup
from selenium import webdriver

# from pandas import Series, DataFrame
# import pandas as pd
# import numpy as np

# import openpyxl
# wb = openpyxl.Workbook()
#out = wb.save('test.xlsx')

# options = Options()
# options.headless = True
chrome_driver_path = 'C:/Users/tjddb/Downloads/chromedriver_win32/chromedriver.exe'
# driver = webdriver.Chrome(executable_path = chrome_driver_path, options=options)
driver = webdriver.Chrome(chrome_driver_path)

out = open("timetable.html",'w', -1, "utf-8")
def lottime_request():
    url = 'http://www.lottecinema.co.kr/LCHS/Contents/ticketing/ticketing.aspx#%EC%A0%84%EC%B2%B4'
    driver.get(url)
    bsObj = BeautifulSoup(driver.page_source, 'html.parser')
    date = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[3]/fieldset/div/label[2]")
    date.click()
    linka = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul/li[3]/span/a")
    linka.click()
    time.sleep(3)

    loc_arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    for s in loc_arr:
        loc_click = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul/li[3]/div/ul/li[" + s + "]/a")
        loc_click.click()
        time.sleep(1)
        location = driver.find_element_by_xpath("//*[@id='content']/div[3]/div[3]/div[2]")
        for p in location.find_elements_by_tag_name('dl'): # 처음 영화데이터 출력
            result_seta = []  #
            result = ""
            final = []
            a = p.text.split(":")
            title = re.split('\n', a[0])[0][2:]
            print(title)
            for i in a:
                b = i[0:2] + i[-2:]
                result_seta.append(b)

            for j in result_seta:
                result += j

            time1 = result[2:-2]

            for i in range(0, len(time1), 4):
                dab = time1[i:i + 4]
                korean = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
                dab2 = re.sub(korean, '', dab)
                final.append(dab2[0:2] + ':' + dab2[-2:])
                for i in final:
                    if i == ' : ':
                        final.remove(' : ')
            sortlist = sorted(final, key=lambda x: (x))
            print(sortlist)
            sortlist.clear()
            final.clear()
            result_seta.clear()
        loc_click.click()


def cgvtime_request():

    # 현재 날짜 구하기
    today=datetime.today()
    # 내일 날짜 구하기
    tomorrow= today + timedelta(days=1)
    tomorrowDate=tomorrow.strftime('%Y%m%d')
    print(tomorrowDate)
    date_arr = [tomorrowDate]
    cgv_arr = ['0207', '0007', '0127', '0275', '0091', '0219', '0209', '0044', '0293', '0228', '0297', '0282', '0142', '0294']
    #          공주     대전   대전터미널 보령    서산     세종   유성온천  천안  천안터미널 청주(서문) 청주성안길 청주율량 청주지웰 청주터미널
    for cgvcode_code in cgv_arr:
        url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=03,205&theatercode=' + cgvcode_code
        for date_code in date_arr:
            url_c = url+'&date='+ date_code
            res = urllib.request.urlopen(url_c).read()
            movie = BeautifulSoup(res, 'html.parser')

            movie = movie.findAll("div", class_="col-times")

            for ul in movie:
                #print(ul.text.split("\n"))
                result_seta = []  #
                result = ""
                final = []
                title = ul.text.replace('\r', '').replace(' ', '').split("\n")
                arr_title = ul.text.replace('\r', '').replace(' ', '').split(":")
                print(title[4])
                for i in arr_title:
                    b = i[0:2] + i[-2:]
                    result_seta.append(b)

                for j in result_seta:
                    result += j

                time1 = result[2:-2]

                for i in range(0, len(time1), 4):
                    dab = time1[i:i + 4]
                    korean = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
                    dab2 = re.sub(korean, '', dab)
                    final.append(dab2[0:2] + ':' + dab2[-2:])
                    for i in final:
                        if i == ' : ':
                            final.remove(' : ')
                sortlist = sorted(final, key=lambda x: (x))
                print(sortlist)
                sortlist.clear()
                final.clear()
                result_seta.clear()

def megatime_request():
    url = 'http://www.megabox.co.kr/?menuId=timetable-cinema'

    driver.get(url)
    bsObj = BeautifulSoup(driver.page_source, 'html.parser')
    linka = driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div/ul/li[5]/a")
    linka.click()
    calander = driver.find_element_by_xpath("//*[@id='container']/div[2]/div/div[1]/div[1]/div[2]/button[2]")
    calander.click()
    loc_arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in loc_arr:
        loc_click = driver.find_element_by_xpath("//*[@id='region_45']/li[" + i + "]/a")
        loc_click.click()
        location = driver.find_element_by_xpath("//*[@id='timeTableCinemaList']")
        for p in location.find_elements_by_tag_name('tr'):
            result_seta = []
            result = ""
            final = []
            a = p.text.split(":")
            # print(a)
            for q in p.find_elements_by_class_name("title"):
                zz = q.text.split("\n")
                title = re.split('\n', zz[1])[0][0:]
                print(title)
            for i in a:
                b = i[0:2] + i[-2:]
                result_seta.append(b)

            for j in result_seta:
                result += j
            time1 = result[2:-2]
            for i in range(0, len(time1), 4):
                dab = time1[i:i + 4]
                korean = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
                dab2 = re.sub(korean, '', dab)
                final.append(dab2[0:2] + ':' + dab2[-2:])
            # for r in p.find_elements_by_class_name("room"):
            for i in final:
                if i == ' : ':
                    final.remove(' : ')
                # r.text.split("\n")  #영화 상영관 정보
            res_arr = []
            res_arr += final
            sortlist = sorted(res_arr, key=lambda x: (x))
            print(sortlist)
            final.clear()
            result_seta.clear()
        res_arr.clear()
        sortlist.clear()
        time.sleep(3)


cgvtime_request()
lottime_request()
megatime_request()