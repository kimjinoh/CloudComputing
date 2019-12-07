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
url = 'http://www.lottecinema.co.kr/LCHS/Contents/ticketing/ticketing.aspx#%EC%A0%84%EC%B2%B4'

driver.get(url)
bsObj = BeautifulSoup(driver.page_source, 'html.parser')

date = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[3]/fieldset/div/label[2]")
date.click()
linka = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul/li[3]/span/a")
linka.click()

loc_arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
for s in loc_arr:
    loc_click = driver.find_element_by_xpath(
        "//*[@id='content']/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul/li[3]/div/ul/li[" + s + "]/a")
    loc_click.click()
    time.sleep(1)

    out=open("lotte.html",'w', -1, "utf-8")
    location = driver.find_element_by_xpath("//*[@id='content']/div[3]/div[3]/div[2]")

    for p in location.find_elements_by_tag_name('dl'):
        print(p.text.split("\n"), file = out)
        print("\n", file = out)
    loc_click.click()