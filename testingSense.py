import time

from sense_hat import SenseHat

# sense = SenseHat()

# O = (255, 255, 255)
# # X = (0, 0, 0) # Black

# white = [
#     O, O, O, O, O, O, O, O,
#     O, O, O, O, O, O, O, O,
#     O, O, O, O, O, O, O, O,
#     O, O, O, O, O, O, O, O,
#     O, O, O, O, O, O, O, O,
#     O, O, O, O, O, O, O, O,
#     O, O, O, O, O, O, O, O,
#     O, O, O, O, O, O, O, O,
# ]

# sense.set_pixels(white)

# sense.clear()

msleep = lambda x: time.sleep(x / 1000.0)

sense = SenseHat()

r1 = 255
g1 = 255
b1 = 255

r2 = 0
g2 = 0
b2 = 0
sense.clear((r1, g1, b1))

#msleep(10)

time.sleep(2)
sense.clear((r2, g2, b2))






