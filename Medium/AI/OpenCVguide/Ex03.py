# 3. Thresholding (fast segmentation)
import cv2 as cv

img_gray = cv.imread("Ex01_output_gray.png")
ret, th = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

# ERROR -
# THRESH_OTSU mode: > 'src_type == CV_8UC1 || src_type == CV_16UC1' > where > 'src_type' is 16 (CV_8UC3)
#ret_otsu, th_otsu = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# Show images
cv.imshow("Binary Threshold", th)
cv.waitKey(0)