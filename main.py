import cv2 as cv
import numpy as np

img = cv.imread('pics/1.png')

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

mask = cv.inRange(hsv, (80, 100, 50), (140, 255, 255))

# cv.imshow('mask', mask)

imask = mask > 0
blue = np.zeros_like(img, np.uint8)
blue[imask] = img[imask]

blur = cv.GaussianBlur(blue, (13,13), 0)

canny = cv.Canny(blur, 10, 30)
cv.imshow('canny', canny)

dilate = cv.dilate(canny, (1, 1))
cv.imshow('dilate', dilate)

cv.waitKey(0)
cv.destroyAllWindows()