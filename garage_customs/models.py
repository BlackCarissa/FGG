from django.db import models
from django.core.files.storage import Storage
from tinymce.models import HTMLField
from django.utils import timezone
from django.forms import ModelForm


class Articles(models.Model):
    link = models.CharField('Ссылка на статью', max_length=50) # Ссылка на статью
    title = models.CharField('Название', max_length=50) # Название статьи
    image = models.ImageField('Фото статьи',upload_to='static/img/')
    anons = models.CharField('Анонс', max_length=250) # Анонс статьи
    text = HTMLField('Полный текст статьи')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
    class Meta:

        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'



