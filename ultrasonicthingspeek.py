  GNU nano 2.7.4                  File: con_ultra.py                            

import os
import time
import sys
import RPi.GPIO as GPIO
import urllib2

myAPI = "BTAPY9NV9RBK330Q"
myDelay = 15 
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 


GPIO_TRIGGER = 23
GPIO_ECHO = 24
try:
   while True:
     print "Ultrasonic Measurement"
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  
     GPIO.setup(GPIO_ECHO,GPIO.IN)      
     GPIO.output(GPIO_TRIGGER, False)
     time.sleep(0.5)
     GPIO.output(GPIO_TRIGGER, True)
     time.sleep(0.00001)
     GPIO.output(GPIO_TRIGGER, False)
     start = time.time()
     while GPIO.input(GPIO_ECHO)==0:
         start = time.time()
     while GPIO.input(GPIO_ECHO)==1:
         stop = time.time()
         elapsed = stop-start
     distance = elapsed * 34300
     distance = distance / 2
     print "Distance : %.1f" % distance
     GPIO.setwarnings(False)
     GPIO.cleanup()
     f = urllib2.urlopen(baseURL + "&field1=%s" % int(distance/5))
     print f.read()
     f.close()

except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
