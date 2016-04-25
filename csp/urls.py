from django.conf.urls import include, url
from django.conf.urls import url
from django.contrib import admin
from cspapp.views import*
from django.conf.urls import patterns
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainpage),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
]
