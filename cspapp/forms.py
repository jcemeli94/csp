from django.forms import ModelForm
from models import *
from django import forms



class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ()


class PostForm(forms.ModelForm):

        class Meta:
            model = User
            fields = ('username','password','email',)

#NO SE USA EN EL REGISTER, SERVIRA PARA INSERTAR POSTS


