from django.conf.urls import url
from django.http import HttpResponse
from django.template.loader import render_to_string


DEBUG = True
SECRET_KEY = '$t@nl3y$0lut!0n$w3b@ut0m@t!0n'
ROOT_URLCONF = __name__
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            "C:/Users/Joe Stanley/Desktop/homeautomation/homeautoapp/homeautoapp/templates"
        ],
    },
]

def cont_outputs(output):
	print(output)

def home(request):
	html = render_to_string('homauto.html', {'B1name': "A", 'B2name': "B", 'B3name': "C"})
	if(request.GET.get('B1')):
		cont_outputs(1)
	elif(request.GET.get('B2')):
		cont_outputs(2)
	elif(request.GET.get('B3')):
		cont_outputs(3)
	elif(request.GET.get('6')):
		print("HI")
	else:
		if(request.GET.urlencode() != ''):
			print("Unauthorized or erroneous access attempt!")
	return HttpResponse(html)


urlpatterns = [
    url(r'^$', home, name='homepage'),
]