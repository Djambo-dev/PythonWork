import cv2

# Task 2 Listening 1.1

# Source Image
source = cv2.imread('images/Monkey-Selfie.jpg')
cv2.imshow('Source Image', source)


# Grayscale Image
gray_image = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)

# Blur Image
blur_image = cv2.blur(gray_image, [3, 3], )

# Gaussian Image
gaussian_blur_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
cv2.imshow('source', gaussian_blur_image)
cv2.waitKey(0)

