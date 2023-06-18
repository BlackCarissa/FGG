from django.shortcuts import render
from .models import Articles


from django.shortcuts import get_object_or_404, redirect
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_http_methods
# Create your views here.

def garagecustoms_home(request):
    News = Articles.objects.all()
    return render(request, 'garage_customs/garagecustoms_home.html',{'News':News})

def garagecustoms_post(request,link):
    News = Articles.objects.all().filter(link=link)
    return render(request,'garage_customs/article.html',{'News':News})
