import cv2
import numpy as np

img = cv2.imread("original.png", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ใช้ GaussianBlur เพื่อลด noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150, apertureSize=3)

lines = cv2.HoughLinesP(
    edges, rho=1, theta=np.pi / 180, threshold=50, minLineLength=30, maxLineGap=5
)

if lines is not None:
    for x1, y1, x2, y2 in lines[:, 0]:
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

cv2.imshow("Hough-transform", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
