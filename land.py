from djitellopy import Tello
import cv2
import time
tello = Tello()

tello.connect()

tello.land()
time.sleep(5)
tello.end()