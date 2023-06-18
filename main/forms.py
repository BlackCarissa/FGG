from django import forms
from .models import Message

class MessageForm(forms.Form):
    FIO = forms.CharField(initial="Иванов Иван Иванович",required=True,label='Ваше ФИО',widget=forms.Textarea)
    number = forms.CharField(initial="+79000000000",required=True,label='Телефон',widget=forms.Textarea)
    check = forms.BooleanField(required=True,label='Я принимаю условия политики обработки персональных данных')
         