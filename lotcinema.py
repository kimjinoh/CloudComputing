import urllib.request
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#chrome_options = Options() chrome_options.add_argument('--headless')
chrome_driver_path = 'C:/Users/wlsdh/git/python/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
url = 'http://www.lottecinema.co.kr/LCHS/Contents/ticketing/ticketing.aspx#%EC%A0%84%EC%B2%B4'
def setdate():
    date = driver.find_element_by_xpath("//input[@id='November27']")
    date.click()
driver.get(url)
bsObj = BeautifulSoup(driver.page_source, 'html.parser')

date = driver.find_element_by_xpath("//label[@for='November27']")
date.click()
linka = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul/li[3]/span/a")
linka.click()
aaaa = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul/li[3]/div/ul/li[6]/a")
aaaa.click()

# location = bsObj.find('div', {'class':'time_aType time4004'})
# movie = location.find_all('dl')
# out=open("lotte.html",'w', -1, "utf-8")
#
# for dl in movie:
#     print(dl, file=out)
