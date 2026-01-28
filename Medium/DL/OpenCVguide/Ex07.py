# 7. Morphological operators — clean up binary masks
import cv2 as cv

img_gray = cv.imread("Ex01_output_gray.png")
ret, binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)

#cv.imshow("opening", opening)
cv.imshow("closing", closing)
cv.waitKey(0)