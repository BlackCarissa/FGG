from django.db import models

class Message(models.Model):
    FIO = models.CharField(max_length=200)
    number = models.CharField(max_length=30)
    def __str__(self):
        return [self.FIO, self.number]
