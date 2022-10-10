from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Blog (models.Model):
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=200)
    subtitulo=models.CharField(max_length=200)
    cuerpo=RichTextField()
    fecha=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField(upload_to='fotos_blog')

    def __str__(self):
        return (f'{self.autor} su Blog')