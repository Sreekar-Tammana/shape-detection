# Import Libraries
import cv2
import numpy as np

# Import Image
# img = cv2.imread('./mobile.jpg')

# Setup webcam and it's height, width
# "link" is provided through external app "IP web cam"
path = "http://192.168.0.122:8080/video"
# "0" for WebCam
cap = cv2.VideoCapture(path)
cap.set(3, 500)
cap.set(4, 500)

# Empty function
def empty(a):
    pass

# Create Trackbars for handling Threshold for Canny edge detector
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)

# Default or starting values
# cv2.createTrackbar("Threshold1", "Parameters", 150, 255, empty)
# cv2.createTrackbar("Threshold2", "Parameters", 255, 255, empty)

# After achieving thresholds values set it to minimum values
# cv2.createTrackbar("Threshold1", "Parameters", 6, 255, empty)
# cv2.createTrackbar("Threshold2", "Parameters", 163, 255, empty)

cv2.createTrackbar("Threshold1", "Parameters", 94, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 57, 255, empty)
cv2.createTrackbar("Area", "Parameters", 5000, 30000, empty)

# Contours Function
def getContours(img, imgContour):
    contour, hie = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contour:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area", "Parameters")

        if area>areaMin:
            # print(area)
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0, 255, 0), 5)
            cv2.putText(imgContour, "Points: " + str(len(approx)), (x+w+20, y+20), cv2.FONT_HERSHEY_COMPLEX, .8, (0, 255, 0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x+w+20, y+45), cv2.FONT_HERSHEY_COMPLEX, .8, (0, 255, 0), 2)

# Loop for webcam
while True:
    success, img = cap.read()

    imgContour = img.copy()

    # Blur image
    imgBlur = cv2.GaussianBlur(img, (7,7), 1)

    # Display image
    cv2.imshow("Original", img)

    # Converting to GrayScale image
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Gray scale", imgGray)

    # Get threshold values from trackbars
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")

    # Converting imgBlur to Canny edge
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    cv2.imshow("Canny image", imgCanny)

    # Dilate Canny image
    kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
    cv2.imshow("Dilate", imgDil)

    getContours(imgDil, imgContour)
    cv2.imshow("Contours", imgContour)
    
    # Quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break