# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 12:29:55 2022

@author: LALO
"""

import numpy as np, cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (255,255,255), 15)#variable, inicio, fin, color, grosor

cv2.rectangle(img, (15,25), (200, 250), (0,255,0), 5)#variable, inicio, fin, color, grosor

cv2.circle(img, (100,63), 55, (0,0,255), -1)#variable, centro, radio, color, grosor

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(0,130), font, 1, (200,255,155), 2, cv2.LINE_AA)#variable, texto, localizacion, fuente, tamaño, color, grosor, tipo de linea 

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()