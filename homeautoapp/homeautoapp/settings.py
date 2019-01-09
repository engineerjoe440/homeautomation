from django.conf.urls import url
from django.http import HttpResponse
from django.template.loader import render_to_string

# Template Directory:
temldir = "C:/Users/Joe Stanley/Desktop/homeautomation/homeautoapp/homeautoapp/templates"
# Label File Directory:
labdir = "C:/Users/Joe Stanley/Desktop/homeautomation/homeautoapp/homeautoapp/Labels.txt"


DEBUG = True
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
print(btn1,btn2,btn3)

def cont_outputs(output):
	print(output)

def home(request):
	html = render_to_string('homauto.html', {'B1name': btn1,
	'B2name': btn2, 'B3name': btn3})
	if(request.GET.get('B1')):
		cont_outputs(1)
	elif(request.GET.get('B2')):
		cont_outputs(2)
	elif(request.GET.get('B3')):
		cont_outputs(3)
	else:
		if(request.GET.urlencode() != ''):
			print("Unauthorized or erroneous access attempt!")
	return HttpResponse(html)


urlpatterns = [
    url(r'^$', home, name='homepage'),
]