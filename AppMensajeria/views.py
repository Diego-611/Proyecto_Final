from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

#Vista Para Enviar Mensajes
@login_required
def viewMessages(request):
    emisor2=request.user
    emisor1=User.objects.get(username=emisor2)
    emisor=emisor1.username
    if request.method=='POST':
        formulario=MensajeFormulario(request.POST)
        if formulario.is_valid():
            msj=formulario.cleaned_data
            receptor2=msj['receptor']
            receptor1=User.objects.filter(username=receptor2)
            if len(receptor1) > 0:
                receptor1=User.objects.get(username=receptor2)
                receptor=receptor1.username
            else:
                return render(request, 'AppMensajeria/sendmessage.html', {'formulario':formulario, 
                'error': f'¡El nombre de Usuario {receptor2} no existe!'})
            mensaje=msj['mensaje']
            sms=Message(emisor=emisor, receptor=receptor, mensaje=mensaje)
            sms.save()
            return render (request, 'AppMensajeria/replymessage.html', {
                'mensaje': f'Mensaje Enviado Correctamente A {receptor}',
                'mensaje2': 'Ahora Solo Queda Esperar A Que La Otra Persona Vea El Mensaje Y Responda',
                'mensaje3': 'O Que Lo Ignore... Lo Que Suceda Primero'
            })
        else:
            return render(request, 'AppMensajeria/sendmessage.html', {'formulario':formulario, 
            'error': '¡Mensaje NO Valido!'})
    else:
        formulario=MensajeFormulario()
        return render(request, 'AppMensajeria/sendmessage.html', {'formulario':formulario})

#Vista Para Enviar Una Noticia
@login_required
def viewBlogMessages(request):
    emisor2=request.user
    emisor1=User.objects.get(username=emisor2)
    emisor=emisor1.username
    if request.method=='POST':
        formulario=MensajeBFormulario(request.POST)
        if formulario.is_valid():
            msj=formulario.cleaned_data
            mensaje=msj['mensaje']
            sms=Message(emisor=emisor, receptor='BlogAdmin_Diego', mensaje=mensaje)
            sms.save()
            return render (request, 'AppMensajeria/replymessage.html', {
                'mensaje': f'Mensaje Enviado Correctamente',
                'mensaje2': 'Revisaremos Manualmente Su Blog',
                'mensaje3': 'En Caso De Ser APROBADO Se Le Enviara UN Mensaje'
            })
        else:
            return render(request, 'AppMensajeria/blogmessage.html', {'formulario':formulario, 
            'error': '¡Mensaje NO Valido!'})
    else:
        formulario=MensajeBFormulario()
        return render(request, 'AppMensajeria/blogmessage.html', {'formulario':formulario})

#Vista de Enviar Mensaje a Usuario
def viewUserMessages(request,id):
    emisor2=request.user
    emisor1=User.objects.get(username=emisor2)
    emisor=emisor1.username
    receptoru=User.objects.get(id=id)
    receptor=receptoru.username
    if request.method=='POST':
        formulario=MensajeBFormulario(request.POST)
        if formulario.is_valid():
            msj=formulario.cleaned_data
            mensaje=msj['mensaje']
            sms=Message(emisor=emisor, receptor=receptor, mensaje=mensaje)
            sms.save()
            return render (request, 'AppMensajeria/replymessage.html', {
                'mensaje': f'Mensaje Enviado Correctamente A {receptor}',
                'mensaje2': 'Ahora Solo Queda Esperar A Que La Otra Persona Vea El Mensaje Y Responda',
                'mensaje3': 'O Que Lo Ignore... Lo Que Suceda Primero'
            })
        else:
            return render(request, 'AppMensajeria/usermessage.html', {'formulario':formulario, 
            'error': '¡Mensaje NO Valido!'})
    else:
        receptor1=User.objects.get(id=id)
        formulario=MensajeBFormulario()
        return render(request, 'AppMensajeria/usermessage.html', {'formulario':formulario, 'receptor1': receptor1})

#Vista De Mensajes Recibidos
@login_required
def viewReceivedMessages(request):
    usuarioUser=request.user
    mensajesR=Message.objects.filter(receptor=usuarioUser).order_by('-fecha')
    return render(request, 'AppMensajeria/receivedmessages.html',{'mensajes':mensajesR})


#Vista De Mensajes Enviados
@login_required
def viewSentMessages(request):
    usuarioUser=request.user
    mensajesE=Message.objects.filter(emisor=usuarioUser).order_by('-fecha')
    return render(request, 'AppMensajeria/sentmessages.html',{'mensajes':mensajesE})

#Vista de Mensajeria
def viewIndexMessage(request):
    return render (request, 'AppMensajeria/message.html')


