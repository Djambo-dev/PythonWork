import cv2

# Task 2 Listening 1.1

# Source Image
source = cv2.imread('images/Monkey-Selfie.jpg')
cv2.imshow('Source Image', source)

# Grayscale Image
gray_image = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)

# Blur Image
blur_image = cv2.blur(gray_image, [3, 3])
cv2.imshow('Blur Image', blur_image)

# Gaussian Image
gaussian_blur_image = cv2.GaussianBlur(gray_image, (3, 3), 1)
cv2.imshow('Gaussian Image', gaussian_blur_image)

# Median Image
median_image = cv2.medianBlur(gray_image, 3)
cv2.imshow('Median Image', median_image)

# Bilateral Image
bilateral_image = cv2.bilateralFilter(gray_image, 9, 75, 75)
cv2.imshow('Bilateral Image', bilateral_image)

cv2.waitKey(0)

