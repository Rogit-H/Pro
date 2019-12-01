# Code based on Python 3.x
# _*_ coding: utf-8 _*_
# __Author: "LEMON"

from bs4 import BeautifulSoup
import requests
import csv

url2 = 'http://www.tianqihoubao.com/weather/top/zhuhai.html'
links = []

links.insert(0, url2)

for url in links:
    rep = requests.get(url)
    content = rep.text.encode(rep.encoding).decode('GB2312')
    # # 直接用requests时，中文内容需要转码

    soup = BeautifulSoup(rep.content, 'html.parser')

    table = soup.table
    #table = soup.find('table')  # 两种方式都可以

    trs = table.find_all('tr')
    trs2 = trs[1:len(trs)]
    list1 = []
    for tr in trs2:
        td = tr.find_all('td')
        row = [i.text for i in td]
        list1.append(row)

    with open('MktDataBJ.csv', 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(list1)