<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {
  background-image: url(/static/circuitboard.png);
  height: 500px; /* You must set a specified height */
  background-position: center; /* Center the image */
  background-repeat: no-repeat; /* Do not repeat the image */
  background-size: cover; /* Resize the background image to cover the entire container */
}
.button {
  background-color: #000080; /* Blue */
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
  cursor: pointer;
  background-color: white; 
  color: black; 
  border: 3px solid #000080;
}
.button:hover {
  background-color: #000080;
  color: white;
  border: 3px solid white;
}
</style>
</head>
<body>

<h2 align="center"><font size="8"><p style="color:white;text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;">Stanley Solutions</p></font></h2>

<form align="center" action="/api/1">
<p style="color:white;text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;"><input type="submit" name="B1" class="button" value={{ button1Name }}>
<b>&emsp; {{ relay1Status }}</b></p>
</form>

<form align="center" action="/api/2">
<p style="color:white;text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;"><input type="submit" name="B2" class="button" value={{ button2Name }}>
<b>&emsp; {{ relay2Status }}</b></p>
</form>

<form align="center" action="/api/3">
<p style="color:white;text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;"><input type="submit" name="B3" class="button" value={{ button3Name }}>
<b>&emsp; {{ relay3Status }}</b></p>
</form>
<h2 align="center"><font size="8"><p style="color:white;text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;">Simple Home Automation</p></font></h2>
</body>

<form align="center" action="/api/reboot">
<p style="color:white;text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;"><input type="submit" name="B4" class="button" value="Reboot">
</p>
</form>

</html>
