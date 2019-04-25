import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) 
import pigpio #importing GPIO library
from gpiozero import MCP3008
ESC=4  #Connect the ESC in this GPIO pin

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0)

max_value = 2000 #change this if your ESC's max value is different or leave it be
min_value = 1000  #change this if your ESC's min value is different or leave it be
pot = MCP3008(0)
xacc = MCP3008(1)

vel = 0
pos = 0
delay = 0.001
while True:

	pot = MCP3008(0)
	xacc = MCP3008(1)
	throttle_percent = pot.value
	pwmout = int(round(1000 + throttle_percent*1000))
	pi.set_servo_pulsewidth(ESC, pwmout)
