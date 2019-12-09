#!/usr/bin/env python3

import urllib.request
from urllib.request import urlretrieve
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import datetime
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
import threading
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(chrome_options = options, executable_path = "/usr/bin/chromedriver")
driver.implicitly_wait(3)
driver.maximize_window()

def fun():
    timer = threading.Timer(86000, fun)
    global out
    out = open("timetable.txt", 'w', -1, "utf-8")
    cgvtime_request()
    lottime_request()
    megatime_request()
    timer.start()
def lottime_request():
    url = 'http://www.lottecinema.co.kr/LCHS/Contents/ticketing/ticketing.aspx#%EC%A0%84%EC%B2%B4'
    driver.get(url)
    bsObj = BeautifulSoup(driver.page_source, 'html.parser')
    date = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[3]/fieldset/div/label[2]")
    date.click()
    linka = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul/li[3]/span/a")
    linka.click()
    time.sleep(3)
    lt_id = 1
    loc_arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    for s in loc_arr:
        if s == '1':
            loc_name = '대전(백화점)점.'
            branch = '대전.'
        elif s == '2':
            loc_name = '대전관저점.'
            branch = '대전.'
        elif s == '3':
            loc_name = '대전둔산(월평동)점.'
            branch = '대전.'
        elif s == '4':
            loc_name = '대전센트럴점.'
            branch = '대전.'
        elif s == '5':
            loc_name = '서산점.'
            branch = '충남.'
        elif s == '6':
            loc_name = '서청주(아울렛)점.'
            branch = '충북.'
        elif s == '7':
            loc_name = '아산터미널점.'
            branch = '충남.'
        elif s == '8':
            loc_name = '청주(성안길)점.'
            branch = '충북.'
        elif s == '9':
            loc_name = '청주용암점.'
            branch = '충북.'
        elif s == '10':
            loc_name = '충주점.'
            branch = '충북.'

        loc_click = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul/li[3]/div/ul/li[" + s + "]/a")
        loc_click.click()
        time.sleep(1)
        location = driver.find_element_by_xpath("//*[@id='content']/div[3]/div[3]")
        time.sleep(1)
        for p in location.find_elements_by_tag_name('dl'): # 처음 영화데이터 출력
            result_seta = []  #
            result = ""
            final = []
            a = p.text.split(":")
            title = re.split('\n', a[0])[0][2:]
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
            data = []
            for abc in sortlist:
                data.append(("L." + str(lt_id) + ".롯데시네마." + branch + loc_name + title).replace(' ','') + "." + abc)
                lt_id += 1
            for abc in range(0, len(sortlist)):
                print(data[abc], file=out)
            #print(sortlist, file = out)
            data.clear()
            sortlist.clear()
            final.clear()
            result_seta.clear()
        loc_click.click()
        time.sleep(1)

def cgvtime_request():

    # 현재 날짜 구하기
    today= datetime.today()
    # 내일 날짜 구하기
    tomorrow= today + timedelta(days=1)
    tomorrowDate=tomorrow.strftime('%Y%m%d')
    #print(tomorrowDate, file = out)
    date_arr = [tomorrowDate]
    cgv_id = 1;
    cgv_arr = ['0207', '0007', '0127', '0275', '0091', '0219', '0209', '0044', '0293', '0228', '0297', '0282', '0142', '0294']
    #          당진     대전   대전터미널 보령    서산     세종   유성온천  천안  천안터미널 청주(서문) 청주성안길 청주율량 청주지웰 청주터미널
    for cgvcode_code in cgv_arr:
        if cgvcode_code == '0207':
            loc_name = '당진점.'
            branch = '충남.'
        elif cgvcode_code == '0007':
            loc_name = '대전점.'
            branch = '대전.'
        elif cgvcode_code == '0127':
            loc_name = '대전터미널점.'
            branch = '대전.'
        elif cgvcode_code == '0275':
            loc_name = '보령점.'
            branch = '충남.'
        elif cgvcode_code == '0091':
            loc_name = '서산점.'
            branch = '충남.'
        elif cgvcode_code == '0219':
            loc_name = '세종점.'
            branch = '세종.'
        elif cgvcode_code == '0209':
            loc_name = '유성온천점.'
            branch = '대전.'
        elif cgvcode_code == '0044':
            loc_name = '천안점.'
            branch = '충남.'
        elif cgvcode_code == '0293':
            loc_name = '천안터미널점.'
            branch = '충남.'
        elif cgvcode_code == '0228':
            loc_name = '청주(서문)점.'
            branch = '충북.'
        elif cgvcode_code == '0297':
            loc_name = '청주성안길점.'
            branch = '충북.'
        elif cgvcode_code == '0282':
            loc_name = '청주율량점.'
            branch = '충북.'
        elif cgvcode_code == '0142':
            loc_name = '청주지웰점.'
            branch = '충북.'
        elif cgvcode_code == '0294':
            loc_name = '청주터미널점.'
            branch = '충북.'
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
                #print(("CGV."+ branch + loc_name+title[4]).split("."), file = out)
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
                data = []
                for abc in sortlist:
                    data.append(("C."+str(cgv_id)+".CGV."+ branch + loc_name+title[4])+"."+abc)
                    cgv_id += 1
                for abc in range(0,len(sortlist)):
                    print(data[abc], file = out)
                data.clear()
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
    mega_id = 1
    loc_arr = ['1', '2', '3',    '4', '5','6','7', '8', '9']
    #          공주 대전 대전중앙로 세종 오창 제천 진천 천안 청주충북대
    for i in loc_arr:
        if i == '1':
            loc_name = '공주점.'
            branch = '충남.'
        elif i == '2':
            loc_name = '대전점.'
            branch = '대전.'
        elif i == '3':
            loc_name = '대전중앙로점.'
            branch = '대전.'
        elif i == '4':
            loc_name = '세종점.'
            branch = '세종.'
        elif i == '5':
            loc_name = '오창점.'
            branch = '충북.'
        elif i == '6':
            loc_name = '제천점.'
            branch = '충북.'
        elif i == '7':
            loc_name = '진천점.'
            branch = '충북.'
        elif i == '8':
            loc_name = '천안점.'
            branch = '충남.'
        elif i == '9':
            loc_name = '청주충북대점.'
            branch = '충북.'
        loc_click = driver.find_element_by_xpath("//*[@id='region_45']/li[" + i + "]/a")
        loc_click.click()
        location = driver.find_element_by_xpath("//*[@id='timeTableCinemaList']")
        locations = location.find_elements_by_tag_name('tr')
        final = []
        res_arr = []
        sortlist = []
        for p in locations:
            result_seta = []
            result = ""
            a = p.text.split(":")
            if(p.find_elements_by_class_name("title")):
                if(sortlist!=[]):
                    data = []
                    for abc in sortlist:
                        data.append(("M." + str(mega_id) + title_arr).replace(' ','') + "." + abc)
                        mega_id += 1
                    for abc in range(0, len(sortlist)):
                        print(data[abc], file = out)
                    
            for q in p.find_elements_by_class_name("title"):
                zz = q.text.split("\n")
                title = re.split('\n', zz[1])[0][0:]
                title_arr = ".메가박스."+ branch + loc_name + title
                final.clear()
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
            res_arr += final
            sortlist = sorted(res_arr, key=lambda x: (x))
            res_arr.clear()
            result_seta.clear()
        data = []
        for abc in sortlist:
            data.append(("M." + str(mega_id) + title_arr).replace(' ','') + "." + abc)
            mega_id += 1
        for abc in range(0, len(sortlist)):
            print(data[abc], file = out)
        #print(sortlist, file = out)
        sortlist.clear()
        time.sleep(3)

fun()
