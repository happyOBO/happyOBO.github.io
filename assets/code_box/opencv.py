#-*- coding:utf-8 -*-
import cv2
import numpy as np

image = cv2.imread('my_char.png',cv2.IMREAD_GRAYSCALE) # 회색조로 이미지 객체 생성

# np 를 이용해 커널 생성
kernel = np.ones((7, 7), np.uint8)
print(kernel)

# make erosion and dilation
open_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
close_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

cv2.imshow('open_image', open_image)

cv2.imshow('close_image', close_image)

cv2.waitKey(50000) 
cv2.destroyAllWindows() 