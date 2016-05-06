from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.views.generic.base import TemplateResponseMixin
from django.core import serializers
from django.shortcuts import render
from django.views.generic.edit import CreateView
from forms import *
from models import *
from django.shortcuts import redirect

# Create your views here.

def mainpage(request):
    return render(request, 'cspapp/principal.html')


class ProjectsList(ListView):
    model = Project
    queryset = Project.objects.all()
    context_object_name = 'projects'
    template_name = 'cspapp/projects_list.html'


class ProjectsDetail(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'cspapp/projects_detail.html'


class ProjectCreate(CreateView):
    model = Project
    template_name = 'cspapp/form.html'
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProjectCreate, self).form_valid(form)


def delete_project(request,rest_pk):
    delRest= Project.objects.get(pk=rest_pk)
    delRest.delete()
    return redirect('http://127.0.0.1:8000/cspapp/projects/')


class CommentCreate (CreateView):
    models = Comment
    template_name = 'cspapp/form.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CommentCreate, self).form_valid(form)


class CommentList(ListView):
    model = Comment
    queryset = Comment.objects.all()
    context_object_name = 'comments'
    template_name = 'cspapp/comment_list.html'