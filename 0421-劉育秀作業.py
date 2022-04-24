# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 00:16:36 2022

@author: 劉育秀
"""

import json   # 解析 json 格式用的
import requests  # 用來上網抓取資料用的

url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json?page=0&size=100"

data = requests.get(url)   # 是stream  串流資料 bytes 位元組

bike = data.text  # 將串流資料轉換成文字內容

content = json.loads(bike) # 將文字格式帶入轉成  json 格式
#content 是json 格式

print(type(data))
print(type(bike))
print(type(content))
print(len(content))
print()
# print(content[0])
# print(content[5])


for row in content:
  print(row['sarea'],'',end='')

print()
AR=input("請輸入欲查詢的區別:")
for row in content:   
  c=row['sarea'].count(AR)
  if c == 1:
      print(AR,":",)
      print("站名：",row['sna'])
      print("可借：",row['sbi'])
      print("可停：",row['bemp'])
      print()
      