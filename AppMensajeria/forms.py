from django import forms
from .models import *
from ckeditor.fields import RichTextFormField

class MensajeFormulario(forms.Form):
    receptor= forms.CharField(max_length=32, label='Para')
    mensaje= RichTextFormField()
    class Meta:
        model = Message
        fields = ['receptor', 'mensaje']

class MensajeBFormulario(forms.Form):
    mensaje= RichTextFormField()
    class Meta:
        model = Message
        fields = ['mensaje']