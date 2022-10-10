from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

#Modelo de los Mensajes
class Message (models.Model):
    emisor= models.CharField(max_length=32)
    receptor= models.CharField(max_length=32)
    mensaje= RichTextField()
    fecha= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.emisor} envio sms a {self.receptor} ')