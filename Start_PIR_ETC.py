
import RPi.GPIO as GPIO
import time
import requests
import string     # helps parse strings
import os

switch1 = 24 # enter your switch gpio number here     PIR
#switch2 = 20 # enter your switch gpio number here     TOUCH

relay1 = 17 # enter your relay gpio number here    SCREEN

state1 = 0
state2 = 0


GPIO.setmode(GPIO.BCM) # you can change this to Board if you prefere
GPIO.setwarnings(False)

GPIO.setup(switch1, GPIO.IN)
#GPIO.setup(switch2, GPIO.IN)
GPIO.setup(relay1, GPIO.OUT)

# set relay off you may need to change this to high if you relay board works active on low, also change state to 1 if this is the case.
GPIO.output(relay1, GPIO.LOW)

while True:

    
#IF ON, then relay ( scherm ) on    
# check if switch is pressed and keep checking
    while GPIO.input(switch1) == 1:     # and GPIO.input(switch2) == 1:
        print "PIR sensor ON..."
        time.sleep(2)
        print "Sensor activated..."
        GPIO.output(relay1, GPIO.HIGH)    #Maybe need to change this to LOW    because of the GIO.Output
        state1 = 1
        time.sleep(100)
            
    
    
    else:
# checks current relay state and changes it to the other.
# else pir is low ( no movement ), scherm uit
        if GPIO.input(switch1) == 0:            # and GPIO.input(switch1) == 1:
            #print "Movement detected! " + (time.strftime("%H:%M:%S"))
            GPIO.output(relay1, GPIO.LOW)     #Maybe need to change this to LOW    because of the GIO.Output
            #DOE JE DINGETJE
            #requests.put('http://192.168.2.175:8080/rest/items/PIR/state', str(ON))
            time.sleep(2)
            state1 = 0


