import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time

# options = Options()
# options.headless = True

chrome_driver_path = 'C:/Users/wlsdh/git/python/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
# driver = webdriver.Chrome(executable_path = chrome_driver_path, options=options)
url = 'http://www.megabox.co.kr/?menuId=timetable-cinema'

driver.get(url)
bsObj = BeautifulSoup(driver.page_source, 'html.parser')
theater = bsObj.find('div', class_="theater_lst")
linka = driver.find_element_by_xpath("//*[@id='container']/div[1]/div[2]/div/ul/li[5]/a")
linka.click()
aaaa = driver.find_element_by_xpath("//*[@id='region_45']/li[9]/a")
aaaa.click()
calander = driver.find_element_by_xpath("//*[@id='schdule_cal_btn']")
calander.click()
date = driver.find_element_by_xpath("//*[@id='datepicker_wrap']/div/div/table/tbody/tr[5]/td[5]/a")
date.click()
time.sleep(3)
out=open("mega.html",'w', -1, "utf-8")
location = driver.find_element_by_xpath("//*[@id='timeTableCinemaList']")

for p in location.find_elements_by_tag_name('tr'):
    print(p.text.split("\n"), file = out)
    print("\n", file = out)
