import cv2 as cv
import numpy as np

img = cv.imread('pics/1.png')

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

mask = cv.inRange(hsv, (80, 100, 50), (140, 255, 255))

# cv.imshow('mask', mask)

imask = mask > 0
blue = np.zeros_like(img, np.uint8)
blue[imask] = img[imask]

gray = cv.cvtColor(blue, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

canny = cv.Canny(gray, 2, 255)
cv.imshow('canny', canny)

cv.waitKey(0)
cv.destroyAllWindows()