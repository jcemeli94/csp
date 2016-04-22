from django.conf.urls import include, url
from django.conf.urls import url
from django.contrib import admin
from cspapp.views import*
from django.conf.urls import patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainpage),
]
