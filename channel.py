# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 23:23:22 2018

@author: Madhav
"""
To create a single channel image
import cv2

image = cv2.imread('D:/DataScience/Intern/SenseHawk/house2.png')

b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0
cv2.imshow('B-RGB', b)
cv2.imwrite('D:/DataScience/Intern/SenseHawk/house_blue.png',b)
cv2.waitKey(0)