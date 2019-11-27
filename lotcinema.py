import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time

options = Options()
options.headless = True
chrome_driver_path = 'C:/Users/wlsdh/git/python/chromedriver.exe'
driver = webdriver.Chrome(executable_path = chrome_driver_path, options=options)
url = 'http://www.lottecinema.co.kr/LCHS/Contents/ticketing/ticketing.aspx#%EC%A0%84%EC%B2%B4'

driver.get(url)
bsObj = BeautifulSoup(driver.page_source, 'html.parser')

date = driver.find_element_by_xpath("//label[@for='November27']")
date.click()
linka = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul/li[3]/span/a")
linka.click()
aaaa = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul/li[3]/div/ul/li[6]/a")
aaaa.click()
time.sleep(3)
out=open("lotte.html",'w', -1, "utf-8")
location = driver.find_element_by_xpath("//*[@id='content']/div[3]/div[3]/div[2]")

for p in location.find_elements_by_tag_name('dl'):
    print(p.text.split("\n"), file = out)
    print("\n", file = out)
