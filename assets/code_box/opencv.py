#-*- coding:utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('approx.png')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret , thr = cv2.threshold(gray_img,100,255,0)

image, contours, hierachy = cv2.findContours(thr,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

approx_image = img
for contour in contours:

    epsilon = 0.02*cv2.arcLength(contour,True)

    approx = cv2.approxPolyDP(contour,epsilon, True)

    approx_image = cv2.drawContours(approx_image, [approx], 0, (0,255,0), 4)

cv2.imshow('approx_image', approx_image)

cv2.waitKey(50000)
cv2.destroyAllWindows()