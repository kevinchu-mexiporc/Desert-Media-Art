# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT
# Kevin Chu
# 9/9/2022
# Desert Media Art - LED
# Resources from Adafruit Industries
# https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/circuitpython-internal-rgb-led

#this is the led setup codes from adafruit tutorial
import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)
    
#this is a function to let the led slowly bright up and slowly get dimmer
def breath(j):
    i = 0
    while (i < j):
        i = i + 1
        led.brightness = i/1000000
    while (i > 0):
        i = i - 1
        led.brightness = i/1000000

#this is a function to let the led to spark
def spark(j):
    while (j < 140000):
        j = j + 1
        if j % 10000 == 0:
            led.brightness = 1
        else:
            led.brightness = 0

#set the variable that will be used in the code for later
j = 0
t = 0
#set the brightness of the led to 0 in the beginning
led.brightness = 0
while True:
    #as the loop run once the state will plus one
    t = t + 1
    #there are 6 states in total that all provide different combinations of led color and brightness
    if t % 6 == 1:
        led[0] = (0, 0, 255)
        j = 100000
        breath(j)
    if t % 6 == 2:
        led[0] = (255, 255, 255)
        j = 100000
        breath(j)
    if t % 6 == 3:
        led[0] = (255, 255, 255)
        j = 0
        spark(j)
    if t % 6 == 4:
        led[0] = (0, 0, 255)
        j = 100000
        breath(j)
    if t % 6 == 4:
        led[0] = (255, 255, 255)
        j = 100000
        breath(j)
    if t % 6 == 0:
        led[0] = (255, 0, 0)
        j = 1000000
        breath(j)

    time.sleep(0.7)
