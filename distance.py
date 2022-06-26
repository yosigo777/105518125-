# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 08:08:44 2022

@author: USER
"""

import math

def rad(x):
     return x * math.pi / 180

def Haversine(lat1,long1,lat2,long2):

      dLat = rad(lat2-lat1)
      dLong = rad(long2-long1)

      v = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(rad(lat1)) * math.cos(rad(lat2)) * math.sin(dLong/2) * math.sin(dLong/2)
      
      
      #math.sqrt平方根
      #math.atan2 = > 給X,Y座標值,產出反正切值
      c = 2 * math.atan2(math.sqrt(v),math.sqrt(1-v))
      
      d = 6371 * c
      return d
  
      