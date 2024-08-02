import cv2

img = cv2.imread('images/image.jpg')
cv2.imshow('Result', img)

cv2.waitKey(0)