#########################################################################################
# Python Django Web Application
# Used for controlling specific outlets in a home-automation scheme on TS-7500
# Written by Joe Stanley
# (c) Stanley Solutions
#########################################################################################

import os
from ts7500 import * # Import control functions for TS7500
from django import forms
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

# Display Unauthorized Access Warning Page
def warning():
    warnhtml = render_to_string('warning.html') # Render Warning HTML page
    print("WARNING: Unauthorized or erroneous access attempt!")
    return(HttpResponse(warnhtml))

# Main Web Interaction Function
def home(request):
    if ( request.method == 'POST' ):
        # POST method is being used!
        if 'B1' in request.POST:
            rly_toggle( RELAY[1] )
        elif 'B2' in request.POST:
            rly_toggle( RELAY[2] )
        elif 'B3' in request.POST:
            rly_toggle( RELAY[3] )
        elif 'B4' in request.POST:
            os.system("reboot")
        else:
            # Unauthorized Access Attempt - Faulty POST
            return( warning() )
    elif(request.method == 'GET' ):
        if(request.GET.urlencode() != ''):
            return( warning() )
    r1, r2, r3 = rly_parse() # Retrieve new status
    html = render_to_string('homauto.html', {'B1name': btn1, 'R1sta': r1,
    'B2name': btn2, 'R2sta': r2, 'B3name': btn3, 'R3sta': r3}) # Render main HTML
    return HttpResponse(html)


urlpatterns = [
    url(r'^$', home, name='homepage'),
]
