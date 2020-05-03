from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
camera = PiCamera()
camera.resolution = (640, 480)
imageCapture = PiRGBArray(camera, size = (640,480))
 
time.sleep(0.2)
 
camera.capture(imageCapture, format="bgr")
image = imageCapture.array
 
cv2.imshow("Captured Image", image)
cv2.waitKey(0)