#########################################################################################
# Python Django Web Application
# Used for controlling specific outlets in a home-automation scheme on TS-7500
# Written by Joe Stanley
# (c) Stanley Solutions
#########################################################################################

import os
from ts7500 import * # Import control functions for TS7500
from django.conf.urls.defaults import url
from django.http import HttpResponse
from django.template.loader import render_to_string

# Template Directory:
temldir = "/home/homeautomation/templates"
# Label File Directory:
labdir = "/home/homeautomation/Labels.txt"

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

# Main Web Interaction Function
def home(request):
	warnhtml = render_to_string('warning.html')
	if(request.GET.get('B1')):
		rly_toggle( RELAY[1] )
	elif(request.GET.get('B2')):
		rly_toggle( RELAY[2] )
	elif(request.GET.get('B3')):
		rly_toggle( RELAY[3] )
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
