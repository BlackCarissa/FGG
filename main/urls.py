
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='home'),
    path('about',views.about, name='about'),
    path('contacts',views.contacts,name='contacts'),
    path('messages',views.Get_Message,name='new_message'),
]
