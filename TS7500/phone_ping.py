#############################################################
# Phone-Detector
# Uses ping option with specified cell-phone IP to determine
# if cell-phone is present on local network.
# Turns on RLY-1 when phone appears,
# turns off RLY-1 when phone leaves.
# Written by Joe Stanley
# (c) Stanley Solutions
#############################################################

import os
from time import sleep as wait
from ts7500 import * # Import control functions for TS7500

prsnt = False
phone = "192.168.1.30"
dly = 30
ctr = 0

while(True):
	# Ping phone
	response = os.system("ping -c 1 " + phone)
	
	# Set RLY-1 if phone wasn't detected previously
	if( prsnt == False and response == 0 ):
		# Set RLY-1
		rly_set( RELAY[1], 1 )
		# Change present status
		prsnt = True
		# Set polling period
		dly = 300
	# Reset RLY-1 if phone leaves but still counted present
	elif( prsnt == True and response != 0 ):
		# Clear RLY-1
		rly_set( RELAY[1], 0 )
		# Change present status
		prsnt = False
		# Set polling period
		dly = 30 # Poll faster when I'm away
	
	# Increment Ping Counter
	ctr = ctr + 1
	if ctr > 20:
		ctr = 0
		# Clear contents of log after 20 pings
		f = open("/home/ping.txt", "w")
		f.close()
	
	# Delay for some time
	wait( dly )