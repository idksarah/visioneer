import cv2 as cv
import numpy as np

img = cv.imread('pics/2.png')

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

mask = cv.inRange(hsv, (80, 100, 50), (140, 255, 255))

imask = mask > 0
blue = np.zeros_like(img, np.uint8)
blue[imask] = img[imask]

blur = cv.GaussianBlur(blue, (15,15), 0)

edges = cv.Canny(blur, 20, 30)
# cv.imshow('canny', edges)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))
edges = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel)

contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# print(len(contours))

img_countours = cv.drawContours(blue, contours, -1,(0,255,0),2)
# cv.imshow('countours', img_countours)
for cnt in contours:
    area = cv.contourArea(cnt)
    if area > 2000:
        rect = cv.minAreaRect(cnt)
        box = cv.boxPoints(rect)
        box = np.int0(box)
        cv.drawContours(img, [box], 0, (0,255,0), thickness=2)
        angle = rect[2]
        print('angle' + str(angle))

cv.imshow('top', img)

# dilate = cv.dilate(canny, (1, 1))
# cv.imshow('dilate', dilate)

cv.waitKey(0)
cv.destroyAllWindows()