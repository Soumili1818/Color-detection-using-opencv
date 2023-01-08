
import cv2
import numpy as np

#mixes the colors and defines the presence of each by showing the resulting color.
#Hue choose the color
#Saturation color density
#Value brightness of color

def nothing(x):
    pass

# Trackbar
cv2.namedWindow("frame")
cv2.createTrackbar("H", "frame", 0, 179, nothing)
cv2.createTrackbar("S", "frame", 255, 255, nothing)
cv2.createTrackbar("V", "frame", 255, 255, nothing)

img_hsv = np.zeros((250, 500, 3), np.uint8)

while True:
    h = cv2.getTrackbarPos("H", "frame")
    s = cv2.getTrackbarPos("S", "frame")
    v = cv2.getTrackbarPos("V", "frame")

#The values to be set are 3 H (0-179) S (0-255) V (0-255) FOR OPEN CV
    img_hsv[:] = (h, s, v)
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow("frame", img_bgr)
    key = cv2.waitKey(1)
    if key == 27:
        break


cv2.destroyAllWindows()

