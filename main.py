# Import Libraries
import cv2

# Setup webcam and it's height, width
cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)

while True:
    success, img = cap.read()

    # Blur image
    imgBlur = cv2.GaussianBlur(img, (7,7), 1)

    # Display image
    cv2.imshow("Original", img)

    # Converting to GrayScale image
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray scale", imgGray)
    
    # Quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

