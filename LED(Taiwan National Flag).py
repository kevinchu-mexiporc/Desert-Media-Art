# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# Kevin Chu
# 9/9/2022
# Desert Media Art - LED
# Resources from Adafruit Industries
# https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython-internal-rgb-led

import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)
i = 0
t = 0
j = 0
led.brightness = 0
while True:
    t = t + 1
    if t % 3 == 1:
        led[0] = (0, 0, 255)
        j = 30000
    if t % 3 == 2:
        led[0] = (255, 255, 255)
        j = 30000
    if t % 3 == 0:
        led[0] = (255, 0, 0)
        j = 100000

    while (i < j):
        i = i + 1
        led.brightness = i/100000
    while (i > 0):
        i = i - 1
        led.brightness = i/100000

    time.sleep(0.5)
