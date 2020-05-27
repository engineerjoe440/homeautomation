#########################################################################################
# Python Bottle Web Application
# Used for controlling specific outlets in a home-automation scheme on TS-7500
# Written by Joe Stanley
# (c) Stanley Solutions
#########################################################################################

# Imports
import os
import bottle
from ts7500 import * # Import control functions for TS7500
from bottle import route, run, template, static_file, redirect, error

# Static Directory:
_static = "/home/homeautomation/static"
_views  = "/home/homeautomation/views"

bottle.TEMPLATE_PATH.insert(0, _views)

# Outlet Labels
file_obj = open(_static + "/Labels.txt", "r")
btn1 = file_obj.readline()
btn2 = file_obj.readline()
btn3 = file_obj.readline()
file_obj.close()

# Indicate Web-Server Start:
os.popen(ctr7500 + " --redledon").readlines() # Not sure if .readlines() is necessary

# Define Static Server
@route('/static/<filename>')
def static_server(filename):
    # Return Static File
    return static_file(filename, root=_static)

# Define API Endpoint Handler
@route('/api/<op>')
def api(op):
    # Test if Integer
    if op.isdigit():
        # Switch on Integer
        case = int(op)
        if case == 1:
            rly_toggle( RELAY[1] )
        elif case == 2:
            rly_toggle( RELAY[2] )
        elif case == 3:
            rly_toggle( RELAY[3] )
    elif op == 'reboot':
        os.system("reboot")
    
    # Redirect to Main Webpage
    redirect('/')

# Define Main Web Endpoint
@route('/')
@route('/index')
def index():
    # Load Relay States
    r1, r2, r3 = rly_parse() # Retrieve new status
    # Load Variable Structure
    template_vars = {
        'button1Name'   : btn1,
        'button2Name'   : btn2,
        'button3Name'   : btn3,
        'relay1Status'  : str(r1),
        'relay2Status'  : str(r2),
        'relay3Status'  : str(r3),
    }
    # Render and Return Template
    return template('index', **template_vars)

# Define 404 Error Response
@error(404)
def error404(error):
    return 'Nothing here, sorry'


# Run Application
run(host='0.0.0.0', port=80)

# END