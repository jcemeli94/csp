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
    url(r'^cspapp/', include('cspapp.urls', namespace = 'cspapp')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),

    url('^register/', CreateView.as_view(
        template_name='register.html',
        form_class=UserCreationForm,
        success_url='http://127.0.0.1:8000/'),name='register'),

    url(r'^delete_project/(?P<rest_pk>\d+)/$', views.delete_project, name='delete_project'),
    url(r'^delete_comment/(?P<rest_pk>\d+)/$', views.delete_comment, name='delete_comment'),
    url(r'^delete_activity/(?P<rest_pk>\d+)/$', views.delete_activity, name='delete_activity'),
    url(r'^delete_answer/(?P<rest_pk>\d+)/$', views.delete_answer, name='delete_answer'),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, })
    ]
