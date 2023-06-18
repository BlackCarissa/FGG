
from django.urls import path
from . import views
from .models import Articles



urlpatterns = [ 
    path('', views.garagecustoms_home, name='garagecustoms_home'),
    path('post/<str:link>/', views.garagecustoms_post, name='post'),
]
