#Programa que genera las medidas de humedad del suelo del sensor.

import RPi.GPIO as GPIO #Libreria para utilizar las GPIO.
import time 		#Libreria para las funciones relacionadas al tiempo. (time)

#set out GPIO numberring to BCM
GPIO.setmode(GPIO.BCM)

#Definir el pin GPIO a usar en este caso el 17.
channel =17
#poner el pin GPIO como Input (entrada).
GPIO.setup(channel,GPIO.IN)

#Funcion para obtener el valor digital.
def medirHumedad():
	valor = GPIO.input(17)
	if valor == 0:
		print("Humedo")
	else:
		print("Seco")
	
	print("sensando humedad")
	#Definir un ciclo infinito para medir la humedad cada 2 segundos.
while True:
	medirHumedad()
	time.sleep(2)