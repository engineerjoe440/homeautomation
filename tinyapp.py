from django.conf.urls import url
from django.http import HttpResponse
from django.template.loader import render_to_string


DEBUG = True
SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh'
ROOT_URLCONF = __name__
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/home/projects/myproject/templates/'
        ],
    },
]


def home(request):
    color = request.GET.get('color', '')
    return HttpResponse('<h1 style="color:' + color + '">Welcome to the Tinyapp\'s Homepage!</h1>')

def about(request):
    title = 'Tinyapp'
    author = 'Vitor Freitas'
    html = render_to_string('about.html', {'title': title, 'author': author})
    return HttpResponse(html)


urlpatterns = [
    url(r'^$', home, name='homepage'),
    url(r'^about/$', about, name='aboutpage'),
]