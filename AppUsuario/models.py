from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class AdditionalUser(models.Model):
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatars', null=True, blank=True)
    descripcion= RichTextField(null=True, blank=True)
    link= models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return (f'{self.usuario} su Informacion')
