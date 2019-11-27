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
#driver = webdriver.Chrome(chrome_driver_path)
url = 'http://www.lottecinema.co.kr/LCHS/Contents/ticketing/ticketing.aspx#%EC%A0%84%EC%B2%B4'
lotdate_file_path = 'C:/Users/wlsdh/git/python/python_crawler_example_01/practice/lottecinemacrawl/'
lotdate_file_name = 'lotdate.txt'
driver.get(url)
bsObj = BeautifulSoup(driver.page_source, 'html.parser')
out=open("lotte.html",'w', -1, "utf-8")
def time_request():
    lotdate_file = open(lotdate_file_path + lotdate_file_name, 'r')
    date = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[3]/fieldset/div/label[2]")
    date.click()
    linka = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul/li[3]/span/a")
    linka.click()
    aaaa = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div[1]/ul/li[3]/div/ul/li[6]/a")
    aaaa.click()
    time.sleep(3)
    location = driver.find_element_by_xpath("//*[@id='content']/div[3]/div[3]/div[2]")

    for p in location.find_elements_by_tag_name('dl'):
        print(p.text.split("\n"), file = out)
        print("\n", file = out)
    for lotdate_code in lotdate_file.readlines():
        date = driver.find_element_by_xpath("//*[@id='content']/div[1]/div/div[3]/fieldset/div/label["+lotdate_code+"]")
        date.click()
        time.sleep(3)
        location = driver.find_element_by_xpath("//*[@id='content']/div[3]/div[3]/div[2]")
        for q in location.find_elements_by_tag_name('dl'):
            print(q.text.split("\n"), file=out)
            print("\n", file=out)

time_request()
