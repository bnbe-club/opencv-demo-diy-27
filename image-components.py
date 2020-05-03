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
 
b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0

g = image.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0

r = image.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0
	
cv2.imshow("Captured Image", image)
cv2.imshow("Blue Component", b)
cv2.imshow("Green Component", g)
cv2.imshow("Red Component", r)

cv2.waitKey(0)