#https://pysource.com/2021/10/19/simple-color-recognition-with-opencv-and-python/

import cv2

#REALTIME
#webcam or with a video, the procedure is identical, only the source changes

cap = cv2.VideoCapture(0)

#With OpenCV, the video stream is processed as a sequence of frames so we
# use the VideoCapture () function and a while loop for processing.

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#import the OpenCV library on our code and then proceed

while True:
    _, frame = cap.read()

    #BGR to CSV conversion is done

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#Identify the center of the screen
#In order to find the color of the object, we identify a point on the screen
#from which to retrieve the three values that make up the color.


    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    # Pick pixel value
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

# we can print the results and have the three values that make up the color
    #Identify the center of the screen
    #extraction of the first value associated with the HSV format,
    # which corresponds to Hue. Based on this we create a set of conditions and show the associated color.

    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    #Show everything on the screen
    #Last step is to show all result on screen, very simple operation to do with OpenCV functions:
    # cv2.rectangle(), cv2.putText() and cv2.circle()



    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()