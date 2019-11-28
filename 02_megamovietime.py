import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time

# options = Options()
# options.headless = True

chrome_driver_path = 'C:/Users/tjddb/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
# driver = webdriver.Chrome(executable_path = chrome_driver_path, options=options)
url = 'http://www.megabox.co.kr/?show=booking&p=step1'

driver.get(url)
bsObj = BeautifulSoup(driver.page_source, 'html.parser')
# theater = bsObj.find('div', class_="theater_lst")
date = driver.find_element_by_xpath("//*[@id='sel_date']/div/ol/li[1]/a")
date.click()
time.sleep(1)
# btn1 = driver.find_element_by_xpath("//*[@id='cinemaList']/ul/li[1]/button")
# btn1.click()
# time.sleep(1)
# loc1 = driver.find_element_by_xpath("//*[@id='body_theater1']/div[1]/ul[1]/li[5]/a")
# loc1.click()
# time.sleep(1)
# loc1_1 = driver.find_element_by_xpath("//*[@id='body_theater1']/div[1]/ul[2]/li[1]/a")
# loc1_1.click()
# time.sleep(1)
# loc1_2 = driver.find_element_by_xpath("//*[@id='body_theater1']/div[1]/ul[2]/li[2]/a")
# loc1_2.click()
# time.sleep(1)
# loc1_3 = driver.find_element_by_xpath("//*[@id='body_theater1']/div[1]/ul[2]/li[3]/a")
# loc1_3.click()
# time.sleep(1)
# check1 = driver.find_element_by_xpath("//*[@id='btnCinemaConfirm']")
# check1.click()
#
# # movie=driver.find_element_by_xpath("//*[@id='showMovieListBtn']")
# # movie.click()
#
# time.sleep(3)
#
# location = driver.find_element_by_xpath("//*[@id='movieTimeList']")
#
# for p in location.find_elements_by_tag_name('li'):
#     print(p.text, file=out)
#
# ref1 = driver.find_element_by_xpath("//*[@id='refreshCinemaBtn']")
# ref1.click()

out = open("02_megamovie.html", 'w', -1, "utf-8")
locs=['1','2','3']
for locat in range(0,3):
    btn2 = driver.find_element_by_xpath("//*[@id='cinemaList']/ul/li[1]/button")
    btn2.click()
    time.sleep(1)
    loc1 = driver.find_element_by_xpath("//*[@id='body_theater1']/div[1]/ul[1]/li[5]/a")
    loc1.click()
    time.sleep(1)
    loccc_file_path='C:/Users/tjddb/git/python/python_crwaler_example01/practice/cgv/'
    loccc_file_name='megamovie.txt'
    loccc_file=open(loccc_file_path+loccc_file_name, 'r')
    for loccc_code in loccc_file.readlines():
        loca =driver.find_element_by_xpath("//*[@id='body_theater1']/div[1]/ul[2]/li["+loccc_code+"]/a")
        loca.click()
    check1 = driver.find_element_by_xpath("//*[@id='btnCinemaConfirm']")
    check1.click()
    time.sleep(3)

    location = driver.find_element_by_xpath("//*[@id='movieTimeList']")

    for p in location.find_elements_by_tag_name('li'):
        print(p.text, file=out)
    ref1 = driver.find_element_by_xpath("//*[@id='refreshCinemaBtn']")
    ref1.click()