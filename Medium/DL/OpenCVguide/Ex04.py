# 4. Denoising: Gaussian vs Median
import cv2 as cv

img_gray = cv.imread("Ex01_output_gray.png")
gauss = cv.GaussianBlur(img_gray, (5, 5), 0)
median = cv.medianBlur(img_gray, 5)

#cv.imshow("GaussianBlur", gauss)
cv.imshow("medianBlur", median)
cv.waitKey(0)