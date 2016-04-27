from django.conf.urls import include, url
from django.conf.urls import url
from django.contrib import admin
from cspapp.views import*
from django.conf.urls import patterns
from django.contrib.auth.views import login, logout
from cspapp.views import *
from cspapp import views


from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainpage),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),

    url('^register/', CreateView.as_view(
        template_name='register.html',
        form_class=UserCreationForm,
        success_url='http://127.0.0.1:8000/'),name='register'),
]

