from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
from .forms import MessageForm
# Create your views here.

def index(request):
    data = {'title': 'Тюнинг ателье FULL GAS GARAGE'}
    return render(request, 'main/index.html', data)

def about(request):
    data = {'title': 'ОБ АВТОМАСТЕРСКОЙ FULL GAS GARAGE'}
    return render(request, 'main/about.html',data)

def contacts(request):
    data = {'title': 'КОНТАКТЫ:'}
    return render(request, 'main/contacts.html',data)

def Get_Message(request):
    FIO=request.POST.get('ClientName')
    number=request.POST.get('tel')
    send=Message(FIO=FIO,number=number)
    send.save()
    return render(request, 'main/return.html')

