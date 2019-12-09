"ONE CLICK MOVIE"
=========
- ### 프로젝트 내용
  ```
  * 자신이 원하는 시간대의 영화가 언제, 어디서 상영하는지 한 눈에 볼 수 있다.
  * CGV, 롯데시네마, 메가박스에서 충청/ 대전/ 세종 지역에서의 각 지점별 영화 시간을 보여준다
  ```
- ### 프로젝트 설명
  ```
  이 프로젝트는 자신이 원하는 시간대의 영화가 언제, 어디서 상영하는지 한 눈에 볼 수 있어 
  그 동안 영화시간을 찾아 여기저기 헤매셨던 당신에게, 편리한 서비스를 제공힌다.
  ```


- ### 사용법  
  ```
  > 영화 랭킹 클릭
    * 매일 9:00 AM에 업데이트 되는 영화 순위 확인 가능
    
  > 상영 정보 클릭
    * 영화 시간표 확인 가능
    * 영화 제목, 지역 선택 
    * 시간순으로 정렬된 영화관 정보 확인 가능 
   ```
   
- ### 환경설정
  #### 크롬 설치
  ```
  $ apt install python3-selenium
  $ wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
  $ sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" 
    >>         /etc/apt/sources.list.d/google.list'
  $ sudo apt-get update
  $ sudo apt-get install google-chrome-stable
  ```
  #### 파이썬 패키지
  ```
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  import datetime 
  import re 
  import urllib.request 
  from datetime import datetime, timedelta 
  import threading 
  import time 
  from bs4 import BeautifulSoup

  import matplotlib.pyplot as plt
  from wordcloud import WordCloud, STOPWORDS
  from threading import Thread
  from time import sleep
  ```

  #### MySQL 테이블 생성
  $mysql -u root -p
  ```sql
  create database movie;
  use movie;

   create table movie(
    mv_id varchar(10) not null,
    mv_num int not null,
    mv_brand varchar(20) ,
    mv_loc varchar(10) ,
    mv_branch varchar(20) ,
    mv_name varchar(100) ,
    mv_time varchar(10) ,
    primary key(mv_id, mv_num)
    );
  ```
  
  #### 실행
    ```
    > ./ltcgvmegacrawl.py
    > timetable.txt 생성
    ```
    ![timetable.PNG](./image/timetable.PNG){: width="100" height="100"}
    ```
    > MySQL -u root -p
    > use movie;
    > LOAD DATA local infile '/home/ubuntu/project/CloudComputing/CloudComputing/integration/timetable.txt'
      into table movie fields terminated by '.';
    > Database에 timetable.txt 데이터 넣기
    ```
    ![data.PNG](./image/data.PNG)
       
