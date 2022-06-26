# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 12:58:03 2022

@author: USER
"""

import psycopg2 #匯入 postgresql資料庫

#連接資料庫

conn = psycopg2.connect(database='d7tdf37ofbfakp',user='fvdaaehbbdpdmp',host='ec2-52-72-56-59.compute-1.amazonaws.com',port='5432')

cursor = conn.cursor() #產生一個資料庫物件

#postgresql 


sql = '''
creat table pharmarcy(
    id serial primary key,
    store varchar(50),
    lat decimal,
    lng decimal,
    address varchar(255),
    phone varchar(30)
    )

'''

cursor.execute(sql)
conn.commit()
conn.close()


    
