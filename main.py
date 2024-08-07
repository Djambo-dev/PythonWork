import cv2
import numpy as np

# Task 1 Listening 1.1

img = cv2.imread('images/image_cv.png')
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Result', img)
cv2.waitKey(0)

