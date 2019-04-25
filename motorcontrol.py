import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you$
import pigpio #importing GPIO library
from gpiozero import MCP3008
ESC=4  #Connect the ESC in this GPIO pin

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0)

max_value = 2000 #change this if your ESC's max value is different or leave it be
min_value = 1000  #change this if your ESC's min value is different or leave it be
pot = MCP3008(0)
xacc = MCP3008(1)

raw_input("Put potentiometer at lowest position then press enter")
vel = 0
pos = 0
delay = 0.001
while True:

	pot = MCP3008(0)
	xacc = MCP3008(1)
	# Convert acceleration from 0-1 range to m/s/s
	# The mapping is 0 -> -3g and 1 -> +3g
	# .5 -> 0g
	xacc_mapped = ((xacc.value * 6)-3) * 9.81

	# Calculate velocity
	vel = vel + xacc_mapped * delay
	print('Velocity', vel)
	# Calculate position
	pos = pos + vel*delay


	ratio = pot.value
	#print(pot.value)
	pwmout = int(round(1000 + ratio*1000))
#	print('PWM', pwmout)
#	print('Xacc', xacc.value)
	pi.set_servo_pulsewidth(ESC, pwmout)
	time.sleep(delay)
