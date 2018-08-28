import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smbus
import time


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) 

TRIG = 18
ECHO = 24

print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
fromaddr= "golurai15011998@gmail.com"
toaddr= "gauravrai15011998@gmail.com"
msg=MIMEMultipart()
msg['From']=fromaddr
msg['to']=toaddr
msg['subject']='garbage level'

bus = smbus.SMBus(1)

bus.write_byte_data(0x53, 0x2C, 0x0A)

bus.write_byte_data(0x53, 0x2D, 0x08)


bus.write_byte_data(0x53, 0x31, 0x08)

time.sleep(0.5)

data0 = bus.read_byte_data(0x53, 0x32)

data1 = bus.read_byte_data(0x53, 0x33)


xAccl = ((data1 & 0x03) * 256) + data0

if xAccl > 511 :
    xAccl -= 1024


data0 = bus.read_byte_data(0x53, 0x34)

data1 = bus.read_byte_data(0x53, 0x35)


yAccl = ((data1 & 0x03) * 256) + data0

if yAccl > 511 : 
    yAccl -= 1024


data0 = bus.read_byte_data(0x53, 0x36)

data1 = bus.read_byte_data(0x53, 0x37)


zAccl = ((data1 & 0x03) * 256) + data0

if zAccl > 511 :
    zAccl -= 1024



 


while True:

  
  GPIO.output(TRIG, False)
  print "Waitng For Sensor To Settle"
  time.sleep(2)

  GPIO.output(TRIG, True)
  time.sleep(0.00001)                      
  GPIO.output(TRIG, False)                 

  while GPIO.input(ECHO)==0:               
    pulse_start = time.time()              

  while GPIO.input(ECHO)==1:               
    pulse_end = time.time()                

  pulse_duration = pulse_end - pulse_start 

  distance = int(pulse_duration * 17150)        

  message = "l=%d" %(distance)
  print distance
  msg.attach(MIMEText(message,'plain'))
  server=smtplib.SMTP('smtp.gmail.com', 25)
  server.starttls()
  server.login(fromaddr, 'password123@')
  text="garbage level exceed"
  text1="bin is not placed properly"
 
 

  if distance < 200:      
    server.sendmail(fromaddr,toaddr,text)
  if (xAccl<0 and zAccl>0 and yAccl>0):
      server.sendmail(fromaddr,toaddr,text1)
  if (yAccl<0 and zAccl>0 and xAccl>0):
      server.sendmail(fromaddr,toaddr,text1)

  server.quit                   
    
