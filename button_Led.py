#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from neopixel import *
import argparse
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Touch Button = GPIO 4
# 
switch1 = 4 # enter your switch gpio number here
switch2 = 7 # TEST FOR GPIO 4 enter your switch gpio number here

GPIO.setup(switch1, GPIO.IN)
GPIO.setup(switch2, GPIO.IN)


# LED strip configuration:
LED_COUNT      = 116      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/$
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor$
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

relay1 = 17 # enter your relay gpio number here

state1 = 0
state2 = 0

# set relay off you may need to change this to high if you relay board works active on low, also change state to 1 if this is the case.

GPIO.setup(relay1, GPIO.OUT)
GPIO.output(relay1, GPIO.LOW)


def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

####
#Real Script starting
####

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

        while True:

# check if switch is pressed and keep checking
            while GPIO.input(switch1) == 0 and GPIO.input(switch2) == 0:
                print "waiting for switch press"
                print "Mirror wordt uitgeschakeld"
                print(GPIO.input(switch1))
                print(GPIO.input(switch2))
                GPIO.output(5, GPIO.HIGH) # High is uitschakelen
                time.sleep(0.5)

            else:

                    if GPIO.input(switch1) == 1: #and GPIO.input(switch2) == 0:
                        print(GPIO.input(switch1))
                        time.sleep(0.5)
                        rainbow(strip)
                        state1 = 1
                        print(GPIO.input(switch1))
                        print(GPIO.input(switch2))


                    elif GPIO.input(switch2) == 1:
                        state2 = 1
                        print "setting PIR AAN"
                        GPIO.output(5, GPIO.LOW) # LOW is aan!
                        time.sleep(1.0)

                    else:
                        print "setting gpio low"
                        state1 = 0
                        state2 = 0
                        GPIO.output(5, GPIO.HIGH) # High is uitschakelen
                        time.sleep(1.0)


# check for switch released and keep checking
            while GPIO.input(switch1) == 1 or GPIO.input(switch2) == 0:
                print "waiting for switch release"
                time.sleep(0.5)

