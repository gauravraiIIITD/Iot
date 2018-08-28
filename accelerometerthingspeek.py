
import os
import time
import sys
from adxl345 import ADXL345
import urllib2

myAPI = "BTAPY9NV9RBK330Q"
myDelay = 15 
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 


adxl345 = ADXL345()
axes = adxl345.getAxes(True)

next_reading = time.time() 



try:
  while True:
        print "ADXL345 on address 0x%x:" % (adxl345.address)
        print "   x = %.3fG" % ( axes['x'] )
        print "   y = %.3fG" % ( axes['y'] )
        print "   z = %.3fG" % ( axes['z'] )



        f = urllib2.urlopen(baseURL + "&field2=%s" % int(axes['x']))
        print f.read()

except KeyboardInterrupt:
    pass





