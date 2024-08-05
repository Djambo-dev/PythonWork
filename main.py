import cv2

# Task 2 Listening 1.1
img = cv2.imread('images/Monkey-Selfie.jpg')
img = cv2.GaussianBlur(img, (3, 3), 0)