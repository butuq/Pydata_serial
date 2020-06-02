import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial
import re
import csv

#initialize serial port
ser = serial.Serial()
ser.port = '/dev/ttyUSB0' #Arduino serial port
ser.baudrate = 115200
ser.timeout = 10 #specify timeout when using readline()
ser.open()
if ser.is_open==True:
	print("\nAll right, serial port now open. Configuration:\n")
	print(ser, "\n") #print serial parametey2

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#ax2 = ax.twinx()  # instantiate a second axes that shares the same x-axis
# fig, ax = plt.subplots() 
last_step = 0
xs = [] #store trials here (n)
y1 = [] #store relative frequency here
y2 = [] #for theoretical probability
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []


# This function is called periodically from FuncAnimation
def animate(i, xs, y1,y2,y3,y4,y5,y6,y7,y8):
    global last_step
    #Aquire and pay2e data from serial port
    # line=ser.readline()      #ascii
    # line_as_list = line.split(b',')
    # i = int(line_as_list[0])
    # relProb = line_as_list[1]
    # relProb_as_list = relProb.split(b'\n')
    # relProb_float = float(relProb_as_list[0])

    ser_bytes = ser.readline()
    decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    txt = decoded_bytes
    print(txt) 
    #Split the string at every white-space character:
    y= re.split("\\x00",txt)
    if(len(y)>1):
        z = y[0] + y[1]
    else:
        z=y[0]
    x = re.split(" ", z)
    print(x)
    #x = x[0:-1]
    

    if(len(x)>8):
        
        csv_generator(x)

        # Add x and y to lists
        # xs.append(i)
        # y1.append(relProb_float)
        # y2.append(0.5)
        xs.append(float(x[0])) #Time
        y1.append(float(x[1])) #y1
        y2.append(float(x[2]))  #y2
        y3.append(float(x[3]))
        y4.append(float(x[4]))
        y5.append(float(x[5]))
        y6.append(float(x[6]))
        y7.append(float(x[7]))
        y8.append(float(x[8]))
        #Volume
        #Flow
        #Pressure
        #Stage
        #Position
        #Target Pos
        #Vel
        #Target Vel
        
        step = float(x[0])
       

        if(step<last_step):
            xs = xs.clear()
            y1 = y1.clear()
            y2 = y2.clear()
            y3 = y3.clear()
            y4 = y4.clear()
            y5 = y5.clear()
            y6 = y6.clear()
            y7 = y7.clear()
            y8 = y8.clear()


            xs = [] #store trials here (n)
            y1 = [] #store relative frequency here
            y2 = [] #for theoretical probability
            y3 = []
            y4 = []
            y5 = []
            y6 = []
            y7 = []
            y8 = []
            # xs.append(i)
            # y1.append(relProb_float)
            # y2.append(0.5)
            xs.append(float(x[0]))
            y1.append(float(x[1]))
            y2.append(float(x[2]))
            y3.append(float(x[3]))
            y4.append(float(x[4]))
            y5.append(float(x[5]))
            y6.append(float(x[6]))
            y7.append(float(x[7]))
            y8.append(float(x[8]))
            #print(x)
        #else:
        #Limit x and y lists to 20 items
            # xs = xs[-100:]
            # y1 = y1[-100:]
            # y2 = y2[-100:]
        # if(len(xs)>80):  
        #     xs = xs[5:]
        #     y1 = y1[5:]
        #     #y2 = y2[5:]
        
        last_step = float(x[0])
        # Draw x and y lists
        
        ax.clear()
        #ax2.clear()
        
        color1 = 'tab:red'
        color2 = 'tab:blue'
        color3 = 'black'
        color4 = 'tab:green'
        color5 = 'tab:purple'
        color6 = 'brown'
        color7 = 'gray'
        color8 = 'orange'
        


        ax.set_xlabel('time (ms)')
        ax.set_ylabel('Values', color=color1)
        ax.plot(xs, y1, label="Volume", color=color1)
        ax.plot(xs, y2, label="Flow", color=color2)
        ax.plot(xs, y3, label="Pressure", color=color3)
        ax.plot(xs, y4, label="Stage", color=color4)
        ax.plot(xs, y5, label="Angular Position", color=color5)
        ax.plot(xs, y6, label="Target Position", color=color6)
        ax.plot(xs, y7, label="Angular Velocity", color=color7)
        ax.plot(xs, y8, label="Target Velocity", color=color8)
        ax.tick_params(axis='y', labelcolor=color1)
        ax.axis([1, 6000, -0.5, 0.6]) #Use for 100 trial demo float(x[9])

        #twin object for two different y-axis on the sample plotimport csvject
        
        # ax2.clear()
        # # color = 'tab:blue'
        # ax2.set_ylabel('otro_y', color=color3)  # we already handled the x-label with ax1
        # ax2.plot(xs, y2, label="Theoretical Probability", color=color3)
        # ax2.tick_params(axis='y', labelcolor=color3)
        # ax2.axis([1, 10000, 0, 1000]) #Use for 100 trial demo
        # fig.tight_layout()
        
        
        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('FABLAB-UTP-VENTILADOR V.1.0')
        #plt.ylabel('Relative frequency')
        plt.legend()
        fig.tight_layout()
        #plt.axis([1, None, 0, 1.1]) #Use for arbitrary number of trials
        



        #print(x)
    
def csv_generator(array):
    with open("Trial1.csv","a") as f:
        writer = csv.writer(f,delimiter=";")
        writer.writerow(array)
    
# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs,y1,y2,y3,y4,y5,y6,y7,y8), interval=10)
plt.show()