# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:48:13 2022

@author: LALO
"""

import numpy as np, cv2

cap = cv2.VideoCapture('people-walking.mp4')
#cap = cv2.VideoCapture(1)
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
 
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    
    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()