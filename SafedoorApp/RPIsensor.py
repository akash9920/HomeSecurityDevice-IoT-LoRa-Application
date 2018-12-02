from time import sleep

import RPi.GPIO as GPIO 


GPIO.setmode(GPIO.BOARD)

GPIO.setup(21, GPIO.OUT)

GPIO.setup(13, GPIO.OUT)

GPIO.setup(2, GPIO.IN)

GPIO.setup(1, GPIO.IN)

cond = GPIO.input(1)


def StartReko():
	
	

