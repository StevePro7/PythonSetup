# 6. Low‑pass → High‑pass (extract details)
import cv2 as cv
import numpy as np

img_gray = cv.imread("Ex01_output_gray.png")
low = cv.GaussianBlur(img_gray, (15, 15), 0)
high = np.uint8(np.clip(img_gray.astype(float) - low.astype(float) + 128, 0, 255))

#cv.imshow("low", low)
cv.imshow("high", high)
cv.waitKey(0)