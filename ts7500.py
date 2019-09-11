#########################################################################################
# Python TS7500 Rugged Computer Control Interface
# Used for controlling specific relays in a home-automation scheme on TS-7500
# Written by Joe Stanley
# (c) Stanley Solutions
#########################################################################################

import os

# Control Directory:
ctr7500 = "/usr/local/bin/ts7500ctl"

# Connection/Pin Dictionarys:
RELAY = { 1:35, 2:37, 3:39 }
DIO_PIN = { 1:40, 2:38, 3:36, 4:34, 5:32, 6:30, 7:28, 8:26 }

# Retrieve Current Status of Relays
def rly_sta():
	cmd = " --getdio"
	cur_out = os.popen(ctr7500 + cmd).readlines()
	out_str = (str(cur_out)[6:])[:-4]
	# print(type(out_str))
	num = int(out_str, 16)
        # print("cur_out",num,type(num))
	return( num )

# Toggle relay
def rly_toggle( pin ):
	"""
	rly_ctrl Function:
	Accepts pin number and toggles specific pin accordingly.
	"""
	# Determine current relay status
	sta = rly_sta()
	# Generate the output integer to toggle relay
	out = sta ^ (1 << pin)
	# Generate strings for command
	dio_dir = " --setdiodir=721554505728"
	dio_set = " --setdio=" + str(out)
	set_cmd = ctr7500 + dio_set + dio_dir
	# Send command
	os.popen( set_cmd ).readlines()
	
	# Check that state changed correctly
	if out != rly_sta():
		print("WARNING: Relay state did not change properly.")
		print("State should be:",out)
		print("But instead is:",rly_sta())

# Set/Clear specific relay
def rly_set( pin, state ):
	# Determine current relay status
	sta = rly_sta()
	rly = ((sta >> pin) & 0x1)
	if rly == state:
		return
	rly_toggle( pin )

# Parse Relay Statuses
def rly_parse():
	txt = ["OFF", "ON"]
	c_sta = rly_sta()
	R1 = txt[ ((c_sta >> 35) & 0x1) ]
	R2 = txt[ ((c_sta >> 37) & 0x1) ]
	R3 = txt[ ((c_sta >> 39) & 0x1) ]
	return(R1,R2,R3)
	
# DIO Pin Status
def get_dio( pin ):
	c_sta = rly_sta()
	sta = ((c_sta >> pin) & 0x1)
	return( sta )

# End of file
