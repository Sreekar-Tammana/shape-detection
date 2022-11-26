# Import Libraries
import cv2

# Setup webcam and it's height, width
cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)

# Empty function
def empty(a):
    pass

# Create Trackbars for handling Threshold for Canny edge detector
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 150, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 255, 255, empty)

# Loop for webcam
while True:
    success, img = cap.read()

    # Blur image
    imgBlur = cv2.GaussianBlur(img, (7,7), 1)

    # Display image
    cv2.imshow("Original", img)

    # Converting to GrayScale image
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray scale", imgGray)

    # Converting imgBlur to Canny edge
    imgCanny = cv2.Canny(imgGray, )
    
    # Quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

