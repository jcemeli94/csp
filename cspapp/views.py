from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from django.views.generic.base import TemplateResponseMixin
from django.core import serializers
from django.shortcuts import render
from django.views.generic.edit import CreateView
from forms import *
from models import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils import timezone

# Create your views here.

def mainpage(request):
    return render(request, 'cspapp/principal.html')

def profile(request,rest_pk):
    profile = User.objects.get(id=rest_pk)
    #projects = Project.objects.all()
    #return render(request, 'cspapp/profile.html', {'projects' : projects} )
    #return render(request, 'cspapp/profile.html', {'profile': profile})
    projects = Project.objects.all()

    context = {'profile': profile, 'projects': projects}
    return render(request, 'cspapp/profile.html', context=context)


class ProjectsList(ListView):
    model = Project
    queryset = Project.objects.all()
    context_object_name = 'projects'
    template_name = 'cspapp/projects_list.html'



class UsersList(ListView):
    model = User
    queryset = User.objects.all()
    context_object_name = 'users'
    template_name = 'cspapp/users_list.html'

class ProjectsDetail(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'cspapp/projects_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectsDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = ProjectReview.RATING_CHOICES
        return context


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


class ActivityDetail(DetailView):
    model = ProjectActivity
    context_object_name = 'activity'
    template_name = 'cspapp/activity_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ActivityDetail, self).get_context_data(**kwargs)
        return context



class ActivityCreate (CreateView):
    models = ProjectActivity
    template_name = 'cspapp/form.html'
    form_class = ActivityForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(ActivityCreate, self).form_valid(form)


class ActivityList(ListView):
    model = Activity
    queryset = Activity.objects.all()
    context_object_name = 'activities'
    template_name = 'cspapp/activities_list.html'


def answer(request, pk):
    act = get_object_or_404(Activity, pk=pk)
    answer = ActivityAnswer(
        body=request.POST['comment'],
        user=request.user,
        project=act)
    answer.save()
    return HttpResponseRedirect(reverse('cspapp:activities_detail', args=(act.id,)))


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


def review(request, pk):
    project = get_object_or_404(Project, pk=pk)
    review = ProjectReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        project=project)
    review.save()
    return HttpResponseRedirect(reverse('cspapp:projects_detail', args=(project.id,)))


def delete_comment(request, rest_pk):
    delRest= Review.objects.get(pk=rest_pk)
    projetpk = ProjectReview.objects.get(pk=rest_pk).project
    delRest.delete()
    return redirect(reverse_lazy('cspapp:projects_detail', kwargs={'pk':projetpk.id}))


def delete_answer(request, rest_pk):
    ans = Answer.objects.get(pk=rest_pk)
    activity = ActivityAnswer.objects.get(pk=rest_pk).project
    ans.delete()
    return redirect(reverse_lazy('cspapp:activities_detail', kwargs={'pk':activity.id}))




def delete_activity(request, rest_pk):
    ans = ProjectActivity.objects.get(pk=rest_pk)
    projetpk = ProjectActivity.objects.get(pk=rest_pk).project
    ans.delete()
    return redirect(reverse_lazy('cspapp:projects_detail', kwargs={'pk':projetpk.id}))