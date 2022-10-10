from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField

#Formulario de Registro
class SignupUserFormulario (UserCreationForm):
    username= forms.CharField(label="Nombre de Usuario")
    first_name= forms.CharField(label='Nombre')
    last_name= forms.CharField(label='Apellido')
    email= forms.CharField(label='Correo @')
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    class Meta:
        model= User
        fields=[
            'username','first_name','last_name','email', 'password1', 'password2'
        ]

#Formulario de Editar UserName
class EditUserFormulario (UserCreationForm):
    username= forms.CharField(label="Nombre de Usuario")
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    class Meta:
        model= User
        fields=['username', 'password1', 'password2']
        help_text= {k: '' for k in fields}

#Formulario de Editar Avatar
class EditAvatarFormulario (forms.Form):
    imagen= forms.ImageField(label= 'Imagen')

#Formulario de Editar Link
class EditLinkFormulario (forms.Form):
    link= forms.CharField(label= 'Link')

#Formulario de Editar Descripcion
class EditDescriptionFormulario (forms.Form):
    descripcion=RichTextFormField()
