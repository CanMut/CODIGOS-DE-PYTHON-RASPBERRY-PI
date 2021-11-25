import MAX6675.MAX6675 as MAX6675   #Importamos la libreria del modulo a usar.
import time                         #Importamos la libreria relacionada al tiempo.

#Definimos nuestros puestos GPIO a usar.
CSK = 25 
CS = 24
DO = 18

sensor = MAX6675.MAX6675(CSK,CS,DO)

try:
    while True:
        Temp = sensor.readTempC()
        print("Temperatura ==> {0:0.2F}".format(Temp))
        time.sleep(1)
except KeyboardInterrupt:
    print("Finalizado...")
