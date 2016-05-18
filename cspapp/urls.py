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

    url(r'^projects/(?P<pk>[a-zA-Z0-9 ]+)/activities/$',
        ActivityList.as_view(),
        name='activity_list'),

    url(r'^projects/(?P<pk>[a-zA-Z0-9 ]+)/activities/create/$',
        ActivityCreate.as_view(),
        name='activity_create'),

    url(r'^activities/(?P<pk>[a-zA-Z0-9 ]+)/$',
        ActivityDetail.as_view(),
        name='activities_detail'),

    url(r'^activities/(?P<pk>[a-zA-Z0-9 ]+)/edit$',
        UpdateView.as_view(
            model=ProjectActivity,
            template_name='cspapp/form.html',
            form_class=ActivityForm),
        name='activity_edit'),

    url(r'^activities/(?P<pk>[a-zA-Z0-9 ]+)/create/$',
        answer,
        name='answer_create'),

    url(r'^projects/(?P<pk>[a-zA-Z0-9 ]+)/reviews/create/$',
        review,
        name='review_create'),
]