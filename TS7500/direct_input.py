#########################################################################################
# Direct Input Control
# Used to take direct input (button controls) and make operations on relay outputs.
# Written by Joe Stanley
# (c) Stanley Solutions
#########################################################################################

import os
from time import sleep as wait
from ts7500 import * # Import control functions for TS7500

while( True ):
	# Check for status changes on three inputs
	if not get_dio( DIO_PIN[1] ):
		rly_toggle( RELAY[1] )	# Toggle RLY-1
		while not get_dio( DIO_PIN[1] ):
			wait( 0.05 )
	elif not get_dio( DIO_PIN[2] ):
		rly_toggle( RELAY[2] )	# Toggle RLY-2
		while not get_dio( DIO_PIN[2] ):
			wait( 0.05 )
	elif not get_dio( DIO_PIN[3] ):
		rly_toggle( RELAY[3] )	# Toggle RLY-3
		while not get_dio( DIO_PIN[3] ):
			wait( 0.05 )
	elif not get_dio( DIO_PIN[5] ):
		os.system("reboot")	# Reboot system!
	
	wait( 0.05 )

# End of file