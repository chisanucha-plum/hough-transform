import cv2
import numpy as np
from hough_space import hough_space #hough_space function from hough_space.py

img = cv2.imread("imgs\\original.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), sigmaX=0)
edge = cv2.Canny(blurred, 100, 250)

hough_img = hough_space(edge)
lines = cv2.HoughLines(edge, rho=1, theta=np.pi/180, threshold=100)

img2 = img.copy()
if lines is not None:
    for line in lines:
        r, theta = line[0]
        #(x0,y0) at the intersection point
        x0 = r*np.cos(theta)
        y0 = r*np.sin(theta)
        #(x1,y1) along the line to the left of (x0,y0) for 1000 units
        x1 =  int(x0-1000*np.sin(theta))
        y1 =  int(y0+1000*np.cos(theta))
        #(x2,y2) along the line to the right of (x0,y0) for 1000 units
        x2 =  int(x0+1000*np.sin(theta))
        y2 =  int(y0-1000*np.cos(theta))
        cv2.line(img2,(x1,y1),(x2,y2),(0,255,0),1)
#ref https://ajgo.blogspot.com/2013/03/hough-line-transform.html

cv2.imwrite("imgs\\Edges.png", edge)
cv2.imwrite("imgs\\Hough-Space.png", hough_img)
cv2.imwrite("imgs\\Hough-Lines.png", img2)

cv2.waitKey()
cv2.destroyAllWindows()
