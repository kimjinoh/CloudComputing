#!/usr/bin/env python3

import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root', password = 'root',db='movie', charset='utf8')

curs = conn.cursor()

sql = "select * from movie"

curs.execute(sql)

rows = curs.fetchall()
print(rows)

conn.close()
