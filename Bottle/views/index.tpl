<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/svg+xml" href="/static/SSLogo.svg">
<style>
body {
  background-image: url(/static/circuitboard.png);
  height: 100%; /* You must set a specified height */
  margin: 0;
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

<div class="bg">

<h2 align="center"><font size="8"><p style="color:white;text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;">Stanley Solutions</p></font></h2>

<form align="center" action="/api/1home">
<p style="color:white;text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;"><input type="submit" name="B1" class="button" value={{ button1Name }}>
<b>&emsp; {{ relay1Status }}</b></p>
</form>

<form align="center" action="/api/2home">
<p style="color:white;text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;"><input type="submit" name="B2" class="button" value={{ button2Name }}>
<b>&emsp; {{ relay2Status }}</b></p>
</form>

<form align="center" action="/api/3home">
<p style="color:white;text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;"><input type="submit" name="B3" class="button" value={{ button3Name }}>
<b>&emsp; {{ relay3Status }}</b></p>
</form>
<h2 align="center"><font size="8"><p style="color:white;text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;">Simple Home Automation</p></font></h2>

<form align="center" action="/api/reboothome">
<p style="color:white;text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;"><input type="submit" name="B4" class="button" value="Reboot">
</p>
</form>

</div>
<br>
<br>
<br>
<br>
<br>
</body>

</html>
