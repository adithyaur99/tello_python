from djitellopy import Tello
import cv2
import time
import serial #import serial library
s=serial.Serial('COM23',9600)
tello = Tello()

tello.connect()

tello.takeoff()
time.sleep(5)
while True:
	msg=s.read()  #Data from Arduino is read serially	
	msg=msg.decode()
	if msg=='S':
		tello.send_rc_control(0,0,0,0)
	if msg=='F':
		tello.send_rc_control(0,100,0,0)
	if msg=='B':

		tello.send_rc_control(0,-100,0,0)
	if msg=='L':

		tello.send_rc_control(-100,0,0,0)
	if msg=='R':

		tello.send_rc_control(100,0,0,0)
	print(msg)

tello.land()
time.sleep(5)
        
tello.end()