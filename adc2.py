from gpiozero import MCP3008
import time
while True:
	pot = MCP3008(0)
	print(pot.value)
	time.sleep(.5)
