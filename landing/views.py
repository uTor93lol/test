from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    projects = ProjectImg.objects.filter(is_active=True)
    return render(request, 'home.html', locals())