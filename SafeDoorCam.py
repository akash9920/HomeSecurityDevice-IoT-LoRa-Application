from picamera import PiCamera
from time import sleep

sense = SenseHat()
camera = PiCamera()


r1 = 255
g1 = 255
b1 = 255

r2 = 0
g2 = 0
b2 = 0

sense.clear((r1, g1, b1))
camera.start_preview()

sleep(1)
camera.capture('image.jpg')
camera.stop_preview()
sense.clear((r2, g2, b2))