from views import *
from django.conf.urls import url
from django.views.generic import DetailView, ListView, UpdateView

urlpatterns = [
    url(r'^projects/$',
        ProjectsList.as_view(),
        name='projects_list'),

    url(r'^projects/create/$',
        ProjectCreate.as_view(),
        name='project_create'),

    url(r'^projects/(?P<pk>[a-zA-Z0-9 ]+)/$',
        ProjectsDetail.as_view(),
        name='projects_detail'),

    url(r'^projects/(?P<pk>[a-zA-Z0-9 ]+)/edit/$',
        UpdateView.as_view(
            model=Project,
            template_name='cspapp/form.html',
            form_class=ProjectForm),
        name='project_edit'),

    url(r'^projects/(?P<pk>[a-zA-Z0-9 ]+)/comment/$',
        CommentList.as_view(),
        name='comment_list'),

    url(r'^projects/(?P<pk>[a-zA-Z0-9 ]+)/comment/create/$',
        CommentCreate.as_view(),
        name='comment_project'),
]