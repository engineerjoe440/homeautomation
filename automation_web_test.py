# Test Web File
from bottle import route, run, template, get, post, Bottle
from bottle import request, error, static_file

Webapp = Bottle()

lights = 'OFF'
fan = 'OFF'

def page(light='OFF', fan='OFF'):
    return(template('''
<!DOCTYPE html>
<html>
<style>
/* The container */
.container {
    display: block;
    position: relative;
    padding-left: 35px;
    margin-bottom: 12px;
    cursor: pointer;
    font-size: 22px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}

/* Hide the browser's default radio button */
.container input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
}

/* Create a custom radio button */
.checkmark {
    position: absolute;
    top: 0;
    left: 0;
    height: 25px;
    width: 25px;
    background-color: #eee;
    border-radius: 50%;
}

/* On mouse-over, add a grey background color */
.container:hover input ~ .checkmark {
    background-color: #ccc;
}

/* When the radio button is checked, add a blue background */
.container input:checked ~ .checkmark {
    background-color: #2196F3;
}

/* Create the indicator (the dot/circle - hidden when not checked) */
.checkmark:after {
    content: "";
    position: absolute;
    display: none;
}

/* Show the indicator (dot/circle) when checked */
.container input:checked ~ .checkmark:after {
    display: block;
}

/* Style the indicator (dot/circle) */
.container .checkmark:after {
 	top: 9px;
	left: 9px;
	width: 8px;
	height: 8px;
	border-radius: 50%;
	background: white;
}
</style>
<body>

<font size="5">
<p align="center" style="margin-top: 0">
<b>Simple Home Automation</b>
</p>
</font>

<form name="control" action="/" method="post" onsubmit="">

<fieldset>
<legend><b>Christmas Lights: {{light}}</b></legend>

<label class="container">On
  <input type="radio" {{'checked="checked"' if (light=='ON') else ""}} name="lights" value="ON">
  <span class="checkmark"></span>
</label>
<label class="container">Off
  <input type="radio" {{'checked="checked"' if (light=='OFF') else ""}} name="lights" value="OFF">
  <span class="checkmark"></span>
</label>
</fieldset>

<fieldset>
<legend><b>Fan: {{fan}}</b></legend>

<label class="container">On
  <input type="radio" {{'checked="checked"' if (fan=='ON') else ""}} name="fan" value="ON">
  <span class="checkmark"></span>
</label>
<label class="container">Off
  <input type="radio" {{'checked="checked"' if (fan=='OFF') else ""}} name="fan" value="OFF">
  <span class="checkmark"></span>
</label>
</fieldset>

<p><input type=submit value=Update></p>

</form>

</body>
</html>

        ''', light=light, fan=fan))

@Webapp.route('/')
def index():
    return( page(lights, fan) )

@Webapp.post('/')
def do_control():
    lights   = request.forms.get('lights')
    fan      = request.forms.get('fan')
    print("I made it")
    print(lights, fan)
    return(page(lights,fan))

@Webapp.error(404)
def error404(error):
    return("Sorry, that link or page seems to be unavailable.")

Webapp.run(host='localhost', port=80)
