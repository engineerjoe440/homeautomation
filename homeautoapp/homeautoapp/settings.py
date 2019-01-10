#########################################################################################
# Python Django Web Application
# Used for controlling specific outlets in a home-automation scheme on TS-7500
# Written by Joe Stanley
# (c) Stanley Solutions
#########################################################################################

import os
from subprocess import call
from django.conf.urls import url
from django.http import HttpResponse
from django.template.loader import render_to_string

# Template Directory:
temldir = "C:/Users/Joe Stanley/Desktop/homeautomation/homeautoapp/homeautoapp/templates"
# Label File Directory:
labdir = "C:/Users/Joe Stanley/Desktop/homeautomation/homeautoapp/homeautoapp/Labels.txt"


DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = '$t@nl3y$0lut!0n$w3b@ut0m@t!0n'
ROOT_URLCONF = __name__
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ temldir ],
    },
]

# Outlet Labels
file_obj = open(labdir, "r")
btn1 = file_obj.readline()
btn2 = file_obj.readline()
btn3 = file_obj.readline()
file_obj.close()

# Send command to OS
def send_control(cmd):
	os.system("mkdir new") # Test only

# Determine control needed
def control(output):
	if output==1:
		# Do something for Relay 1
		send_control(output)
	elif output ==2:
		# Do something for Relay 2
		x = 1
	elif output ==3:
		# Do something for Relay 3
		x = 1
	else:
		print("WARNING: Unexpected function call.\nValue outside of range [1,3].")
	print(output)

def home(request):
	html = render_to_string('homauto.html', {'B1name': btn1,
	'B2name': btn2, 'B3name': btn3})
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
	return HttpResponse(html)


urlpatterns = [
    url(r'^$', home, name='homepage'),
]