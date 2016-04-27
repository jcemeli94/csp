from django.shortcuts import render
from forms import *
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.

def mainpage(request):
    return render(request, 'cspapp/principal.html')
