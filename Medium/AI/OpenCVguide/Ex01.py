# 1. Read, convert and save
import cv2 as cv


# Read a color image (OpenCV returns BGR)
img = cv.imread("LilEvelKnievelSMS.png")
#cv.imshow("LilEvelKnievelSMS", img)
#cv.waitKey(0)


# Convert to grayscale for most classical ops
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("LilEvelKnievelSMS", img_gray)
cv.waitKey(0)
cv.imwrite("Ex01_output_gray.png", img_gray)