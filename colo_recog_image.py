import cv2
img = cv2.imread("blue_background.jpg")
print(img)
cv2.imshow("Img",img)
cv2.waitKey(0)

#Importing a completely blue image and printing the results with python will result in an array
# showing the values of each color cell. Each color is always composed of 3 values between 0 and 255
# with this sort Blue – Green – Red.