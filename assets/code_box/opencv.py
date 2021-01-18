#-*- coding:utf-8 -*-
import cv2


img = cv2.imread('noise.png')
# src, d, sigmaColor, sigmaSpace
# d : 필터링에 이용하는 이웃한 픽셀의 지름
# sigmaColor : 컬러 공간의 시그마 공간 정의
# sigmaSpace : 시그마 필터 조정, 값이 길수록 긴밀하게 주변 픽셀 영향
blur = cv2.bilateralFilter(img,5,75,75)
blur2 = cv2.bilateralFilter(img,10,75,75)

cv2.imshow('Original', img)
cv2.imshow('Result', blur)
cv2.imshow('Result2', blur2)

cv2.waitKey(100000)
cv2.destroyAllWindows()