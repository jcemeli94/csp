from django.forms import ModelForm
from models import *
from django import forms


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ('author', 'project',)


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ()


class PostForm(forms.ModelForm):

        class Meta:
            model = User
            fields = ('username', 'password' ,'email',)


class ActivityForm(forms.ModelForm):
    class Meta:
        model = ProjectActivity
        exclude = ('user', 'date', 'creator',)

#NO SE USA EN EL REGISTER, SERVIRA PARA INSERTAR POSTS


