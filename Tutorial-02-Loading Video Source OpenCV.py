# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 12:11:39 2022

@author: LALO
"""

import cv2, numpy as np

cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    out.write(frame)
    
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()