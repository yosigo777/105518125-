# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 08:57:01 2022

@author: USER
"""
from distance import Haversine

#我要計算台中公園 距 一中夜市 及宮原眼科之間的距離

tcdan = Haversine(24.1448185,120.6822875,24.1485546,120.6825456)

ice = Haversine(24.1448185,120.6822875,24.1378278,120.6813665)
                
print("台中公園至一中街的距離 :",tcdan)

print("台中公園至宮原眼科的距離:",ice) 
                
                
                