import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) 

TRIG = 18
ECHO = 24

print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
fromaddr= "theshieldinternity@gmail.com"
toaddr= "gauravrai15011998@gmail.com"
msg=MIMEMultipart()
msg['From']=fromaddr
msg['to']=toaddr
msg['subject']='garbage level'
 


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
 
 

  if distance < 200:      
    server.sendmail(fromaddr,toaddr,text)
  server.quit                   
    
