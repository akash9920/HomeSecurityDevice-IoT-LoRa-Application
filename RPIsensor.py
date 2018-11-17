from time import sleep

import RPi.GPIO as GPIO 


GPIO.setmode(GPIO.BOARD)

GPIO.setup(21, GPIO.OUT)

GPIO.setup(13, GPIO.OUT)

GPIO.setup(2, GPIO.IN)

GPIO.setup(1, GPIO.IN)

cond = GPIO.input(1)


def TestJhanvi():
	print("Jhanvi ko uthana na pade")


def startAPP():
	if GPIO.input(2) is True:
		print("The switch is closed")
		TestJhanvi()
	else : print("Waitin<F10><F9><F8><F7>")


def StartReko():
	if x is True:
		TestJhanvi()
		print("The switch is closed")
		

