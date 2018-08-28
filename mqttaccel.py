  import os
import time
import sys
from adxl345 import ADXL345
import paho.mqtt.client as mqtt
import json
THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'joxL7VjUG2oV0kydZSE5'
INTERVAL=2  
adxl345 = ADXL345()
axes = adxl345.getAxes(True)

next_reading = time.time() 

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()
try:
     while True:
        print "ADXL345 on address 0x%x:" % (adxl345.address)
        print "   x = %.3fG" % ( axes['x'] )
        print "   y = %.3fG" % ( axes['y'] )
        print "   z = %.3fG" % ( axes['z'] )



        client.publish('v1/devices/me/telemetry', json.dumps(axes), )

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
