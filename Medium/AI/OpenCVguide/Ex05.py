# 5. Edge detectors: Sobel & Laplacian
import cv2 as cv
import numpy as np

img_gray = cv.imread("Ex01_output_gray.png")
sobelx = cv.Sobel(img_gray, cv.CV_64F, 1, 0, ksize=3)
sobely = cv.Sobel(img_gray, cv.CV_64F, 0, 1, ksize=3)
sobel = np.hypot(sobelx, sobely).astype(np.uint8)

#cv.imshow("sobelx", sobelx)
#cv.imshow("sobely", sobely)
cv.imshow("sobel", sobel)

cv.waitKey(0)