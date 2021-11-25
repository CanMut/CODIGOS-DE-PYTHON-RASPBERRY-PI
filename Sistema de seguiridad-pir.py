from picamera import PiCamera
from time import sleep
import smtplib
gmail_user = 'correoemisor@gmail.com'  
gmail_password = 'Contraseña'
import time
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import RPi.GPIO as GPIO
import time

toaddr = 'correoreceptor@gmail.com'
me = 'correoemisor@gmail.com'
Subject='Alerta de Seguridad'

GPIO.setmode(GPIO.BCM)

P=PiCamera()
P.resolution= (1024,768)
P.start_preview()
    
GPIO.setup(23, GPIO.IN)
while True:
    if GPIO.input(23):
        print("Movimiento...")
        #camera warm-up time
        time.sleep(1)
        P.capture('movimiento.jpg')
        time.sleep(4)
        subject='Alerta, Alguien se encuentra en tu casa!!'
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = toaddr
        
        fp= open('movimiento.jpg','rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)

        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()
