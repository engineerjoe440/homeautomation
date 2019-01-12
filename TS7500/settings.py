#########################################################################################
# Python Django Web Application
# Used for controlling specific outlets in a home-automation scheme on TS-7500
# Written by Joe Stanley
# (c) Stanley Solutions
#########################################################################################

import os
from django.conf.urls.defaults import url
from django.http import HttpResponse
from django.template.loader import render_to_string

# Template Directory:
temldir = "/home/homeautomation/templates"
# Label File Directory:
labdir = "/home/homeautomation/Labels.txt"
# Control Directory:
ctr7500 = "/usr/local/bin/ts7500ctl"

# Indicate Web-Server Start:
os.popen(ctr7500 + " --redledon").readlines() # Not sure if .readlines() is necessary

DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = '$t@nl3y$0lut!0n$w3b@ut0m@t!0n'
ROOT_URLCONF = __name__

TEMPLATE_DIRS = (
    temldir,
)

# Outlet Labels
file_obj = open(labdir, "r")
btn1 = file_obj.readline()
btn2 = file_obj.readline()
btn3 = file_obj.readline()
file_obj.close()

# Retrieve Current Status of Relays
def rly_sta():
	cmd = " --getdio"
	cur_out = os.popen(ctr7500 + cmd).readlines()
	out_str = (str(cur_out)[6:])[:-4]
	# print(type(out_str))
	num = int(out_str, 16)
        # print("cur_out",num,type(num))
	return( num )

# Parse Relay Statuses
def rly_parse():
	txt = ["OFF", "ON"]
	c_sta = rly_sta()
	R1 = txt[ ((c_sta >> 35) & 0x1) ]
	R2 = txt[ ((c_sta >> 37) & 0x1) ]
	R3 = txt[ ((c_sta >> 39) & 0x1) ]
	return(R1,R2,R3)

# Determine control needed
def control(output):
	if output==1:
		# Do something for Relay 1
		sta = rly_sta()
		out = sta ^ (1 << 35)
	elif output ==2:
		# Do something for Relay 2
		sta = rly_sta()
		out = sta ^ (1 << 37)
	elif output ==3:
		# Do something for Relay 3
		sta = rly_sta()
		out = sta ^ (1 << 39)
	else:
		print("WARNING: Unexpected function call.\nValue outside of range [1,3].")
		return
	#print(output)
	
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

def home(request):
	warnhtml = render_to_string('warning.html')
	if(request.GET.get('B1')):
		control(1)
	elif(request.GET.get('B2')):
		control(2)
	elif(request.GET.get('B3')):
		control(3)
	else:
		if(request.GET.urlencode() != ''):
			print("WARNING: Unauthorized or erroneous access attempt!")
			return(HttpResponse(warnhtml))
	r1, r2, r3 = rly_parse() # Retrieve new status
	html = render_to_string('homauto.html', {'B1name': btn1, 'R1sta': r1,
	'B2name': btn2, 'R2sta': r2, 'B3name': btn3, 'R3sta': r3})
	return HttpResponse(html)


urlpatterns = [
    url(r'^$', home, name='homepage'),
]
