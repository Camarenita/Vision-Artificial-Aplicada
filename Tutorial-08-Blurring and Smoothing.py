# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:05:12 2022

@author: LALO
"""

import numpy as np, cv2

cap = cv2.VideoCapture(1)

while True:

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([150,150,50])
    upper_red = np.array([185,255,150])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)
    
    blur = cv2.GaussianBlur(res,(15,15),0)
    
    median = cv2.medianBlur(res,15)
    
    bilateral = cv2.bilateralFilter(res,15,75,75)
    
    cv2.imshow('Original',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    #cv2.imshow('smoothed',smoothed)
    cv2.imshow('blur',blur)
    cv2.imshow('median',median)
    cv2.imshow('bilateral Blur',bilateral)
    

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()