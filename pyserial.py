import serial
import time
import csv
import base64
import re





#Definir puerto y baudrate
ser = serial.Serial('/dev/ttyUSB0', baudrate=115200)

ser.flushInput()


while True:
    try:
	#Cambiar segun la cantidad de datos a medir, todos en Serial.println
	#TODO Sistema para incluir titulos para los datos, por ahora solo puedes guiarte por el orden que tienen el cual suele desfasarse.
        ser_bytes = ser.readline()
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        txt = decoded_bytes

        #Split the string at every white-space character:
        x = re.split(" ", txt)
        
        with open("120-20-70_TEST_5.csv","a") as f:
            print(x)
            # for m in range(10):
            if(len(x)>1):
                writer = csv.writer(f,delimiter=";")
                writer.writerow(x)
                
                
    except:
        print("Keyboard Interrupt")
        break
