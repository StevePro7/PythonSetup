# 2. Histograms — why your Y axis sometimes goes to 8000+
import cv2 as cv
import matplotlib.pyplot as plt

img_gray = cv.imread("Ex01_output_gray.png")
hist = cv.calcHist([img_gray], [0], None, [256], [0, 256])
hist_percent = hist.ravel() / img_gray.size * 100

plt.plot(hist_percent); plt.title('Histogram (percent)')

plt.figure(); plt.plot(hist.ravel());
plt.yscale('log'); plt.title('Histogram (log scale)')

plt.show()