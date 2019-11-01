
import RPi.GPIO as GPIO
import time
import requests
import string     # helps parse strings
import os

switch1 = 24 # enter your switch gpio number here     PIR
#switch2 = 20 # enter your switch gpio number here     TOUCH

relay1 = 17 # enter your relay gpio number here    SCREEN

#state1 = 0
#state2 = 0


GPIO.setmode(GPIO.BCM) # you can change this to Board if you prefere
GPIO.setwarnings(False)

GPIO.setup(switch1, GPIO.IN)
#GPIO.setup(switch2, GPIO.IN)
GPIO.setup(relay1, GPIO.OUT)

# set relay off you may need to change this to high if you relay board works active on low, also change state to 1 if this is the case.
GPIO.output(relay1, GPIO.LOW)

while True:

# check if switch is pressed and keep checking
    while GPIO.input(switch1) == 1:     # and GPIO.input(switch2) == 1:
        print "PIR sensor ON..."
        time.sleep(2)
        print "Sensor activated..."
        GPIO.output(relay1, GPIO.HIGH)
        time.sleep(10)
            
    
    
    else:
# checks current relay state and changes it to the other.
        if GPIO.input(switch1) == 0:            # and GPIO.input(switch1) == 1:
            print "Movement detected! " + (time.strftime("%H:%M:%S"))
            GPIO.output(relay1, GPIO.LOW)
            #DOE JE DINGETJE
            #requests.put('http://192.168.2.175:8080/rest/items/PIR/state', str(ON))
            time.sleep(2)
            state1 = 0



        elif GPIO.input(switch1) == 1 and GPIO.input(switch2) == 0:
            #elif state2 == 0:
            print "Setting SWITCH 2  gpio high"
            requests.put('http://192.168.2.175:8080/rest/items/Touch/state', str(average))
            state2 = 1
            GPIO.output(relay1, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(relay1, GPIO.LOW)
            time.sleep(3)
            GPIO.output(relay2, GPIO.LOW)
            state2 = 0
            time.sleep(1)
        else:
            print "setting gpio low"
            state1 = 0
            state2 = 0
            GPIO.output(relay1, GPIO.LOW)
            time.sleep(1)

# check for switch released and keep checking
    while GPIO.input(switch1) == 0 or GPIO.input(switch2) == 0:
        print "waiting for switch release"
        time.sleep(0.5)



