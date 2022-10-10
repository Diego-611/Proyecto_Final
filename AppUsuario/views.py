from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from AppUsuario.models import AdditionalUser
from .forms import *
from AppMensajeria.models import Message


#Vista de Registro de Usuario
def viewSignup (request):
    if request.method== 'POST':
        formulario=SignupUserFormulario(request.POST)
        if formulario.is_valid():
            usuario= formulario.cleaned_data['username']
            formulario.save()
            userCustomization=User.objects.get(username=usuario)
            additionaluser=AdditionalUser(usuario=userCustomization)
            additionaluser.save()
            default=AdditionalUser.objects.get(usuario=userCustomization)
            default.imagen= 'avatars/imagenpordefecto.png'
            default.descripcion='Sin Informacion'
            default.link='...'
            default.save()
            return render(request, 'AppUsuario/registered.html', {'bienvenida': f'¡BIENVENIDO {usuario}, YA FORMAS PARTE DE ESTA APPLICACION WEB!'})
        else:
            formulario=SignupUserFormulario()
            return render(request, 'AppUsuario/signupUser.html', {'formulario':formulario, 'error': 'Registro NO Valido'})
    else:
        formulario=SignupUserFormulario()
        return render(request, 'AppUsuario/signupUser.html', {'formulario':formulario})

#Vista de Ingreso al Usuario
def viewLogin (request):
    if request.method== 'POST':
        formulario=AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario= request.POST['username']
            clave= request.POST['password']
            verifiacion=authenticate(username=usuario,password=clave)
            if verifiacion is not None:
                login(request,verifiacion)
                return render(request, 'AppUsuario/registered.html', {'bienvenida': f'¡BIENVENIDO NUEVAMENTE {usuario}!'})
            else:
                return render(request, 'AppUsuario/loginUser.html',{'formulario':formulario,})
        else:
            return render(request, 'AppUsuario/loginUser.html',{'formulario':formulario,})
    else:
        formulario=AuthenticationForm()
        return render(request, 'AppUsuario/loginUser.html', {'formulario':formulario})

#Vista de Edicion de Usuario
@login_required
def viewEditUserName (request):
    if request.method=='POST':
        formulario=EditUserFormulario(request.POST)
        if formulario.is_valid():
            usuario=User.objects.get(username=request.user)
            olduser=usuario.username
            usuario.username=formulario.cleaned_data['username']
            usuario.save()
            user=usuario.username
            oldemisor=Message.objects.filter(emisor=olduser)
            for u in oldemisor:
                u.emisor=user
                u.save()
                oldreceptor=Message.objects.filter(receptor=olduser)
            for u in oldreceptor:
                u.receptor=user
                u.save()
            return render (request, 'AppUsuario/edited.html', {
            'mensaje': '¡Editaste Correctamente Tu Nombre De Usuario!',
            'mensaje2': f'Espero Te Guste Tu Nuevo Nombre {user}'
            })
        else:
            return render(request, 'AppUsuario/editUser.html', {'formulario':formulario,})
    else:
        formulario=EditUserFormulario(instance=request.user)
        return render(request, 'AppUsuario/editUser.html', {'formulario':formulario})

#Vista de Eliminar Usuario
@login_required
def viewDeleteUser(request):
    if request.method== 'POST':
        formulario=AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario= request.POST['username']
            clave= request.POST['password']
            verifiacion=authenticate(username=usuario,password=clave)
            if verifiacion is not None:
                deleteUser=request.user
                delete=User.objects.get(username=deleteUser)
                userdelete=delete.username
                smsEdelete=Message.objects.filter(emisor=userdelete)
                smsEdelete.delete()
                smsRdelete=Message.objects.filter(receptor=userdelete)
                smsRdelete.delete()
                delete.delete()
                return render(request, 'AppBlog/index.html')
            else:
                return render(request, 'AppUsuario/deleteUser.html',{'formulario':formulario,})
        else:
            return render(request, 'AppUsuario/deleteUser.html',{'formulario':formulario,})
    else:
        formulario=AuthenticationForm()
        return render(request, 'AppUsuario/deleteUser.html', {'formulario':formulario})


#Vista de Edicion
@login_required
def viewEdit(request):
    return render(request, 'AppUsuario/edit.html')

#Vista de Login Flash
def viewLoginFlash(request):
    return render(request, 'AppUsuario/loginflash.html')

#Vista de Edicion de Biografia
@login_required
def viewEditDescription (request):
    user=request.user
    if request.method== 'POST':
        formulario=EditDescriptionFormulario(request.POST)
        if formulario.is_valid():
            descripcion1=User.objects.get(username=request.user)
            descripcion=AdditionalUser.objects.get(usuario=descripcion1)
            descripcion.descripcion= formulario.cleaned_data['descripcion']
            descripcion.save()
            return render(request, 'AppUsuario/edited.html', {
            'mensaje': f'¡Editaste Correctamente Tu Biografia {user}!', 
            'mensaje2': 'Ahora Todos Podran Saber Un Poco Mas De Ti',
            'mensaje3':'¡ESPEREMOS QUE ESA BIOGRAFIA SEA TOTALMENTE CRISTIANA Y APROBADA POR EL SEÑOR TODO PODEROSO!'
            })
        else:
            return render(request, 'AppUsuario/editDescription.html', {'formulario':formulario, 'usuario': request.user,
            'error': '¡Biografia NO Valida!'})
    else:
        formulario=EditDescriptionFormulario()
        return render(request, 'AppUsuario/editDescription.html', {'formulario':formulario})

#Vista de Edicion de Link
@login_required
def viewEditLink (request):
    user=request.user
    if request.method== 'POST':
        formulario=EditLinkFormulario(request.POST)
        if formulario.is_valid():
            link1=User.objects.get(username=request.user)
            link=AdditionalUser.objects.get(usuario=link1)
            link.link= formulario.cleaned_data['link']
            link.save()
            return render(request, 'AppUsuario/edited.html', {
            'mensaje': f'¡Editaste Correctamente Tu Link {user}!',
            'mensaje2':'Ahora Todos Podran Entrar A Tu Link',
            'mensaje3':'¡ESPEREMOS QUE EL LINK NO LLEVE A NINGUN LUGAR SEXUAL... GUARRO!'
            })
        else:
            return render(request, 'AppUsuario/editLink.html', {'formulario':formulario, 'usuario': request.user,
            'error': '¡Link NO Valido!'})
    else:
        formulario=EditLinkFormulario()
        return render(request, 'AppUsuario/editLink.html', {'formulario':formulario, })
        

#Vista de Editar Avatar del Usuario
@login_required
def viewEditAvatar (request):
    user=request.user
    if request.method== 'POST':
        formulario=EditAvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            avatar1=User.objects.get(username=request.user)
            avatar=AdditionalUser.objects.get(usuario=avatar1)
            avatar.imagen= formulario.cleaned_data['imagen']
            avatar.save()
            return render(request, 'AppUsuario/edited.html', {
            'mensaje': f'¡Editaste Correctamente Tu Avatar {user}!',
            'mensaje2':'Ahora Todos Podran Ver Tu Nueva Foto Facherisima',
            'mensaje3': '¡ESPEREMOS QUE LA IMAGEN NO SEA NADA PERVERTIDO... GUARRO!',
            'imagen': getAvatar(request),
            })
        else:
            return render(request, 'AppUsuario/editAvatar.html', {'formulario':formulario, 'usuario': request.user,
            'error': '¡Imagen NO Valida!'})
    else:
        formulario=EditAvatarFormulario()
        return render(request, 'AppUsuario/editAvatar.html', {'formulario':formulario, })

#Vista que Muestra el Perfil del Usuario
@login_required
def viewProfile(request):
    usuario=User.objects.get(username=request.user)
    usuarioA=AdditionalUser.objects.get(usuario=usuario)
    imagen=usuarioA.imagen.url
    nusuario=usuario.username
    nombre=usuario.first_name
    apellido=usuario.last_name
    email=usuario.email
    descripcion=usuarioA.descripcion
    link=usuarioA.link
    return render(request, 'AppUsuario/profile.html', {'imagen':imagen,'nusuario':nusuario,'nombre':nombre,'apellido':apellido,
    'email':email,'descripcion':descripcion,'link':link})

#Vista que Muestra el Perfil del Creador
@login_required
def viewUProfile(request,id):
    usuario=User.objects.get(id=id)
    usuarioA=AdditionalUser.objects.get(usuario=usuario)
    user=usuario.id
    imagen=usuarioA.imagen.url
    nusuario=usuario.username
    nombre=usuario.first_name
    apellido=usuario.last_name
    email=usuario.email
    descripcion=usuarioA.descripcion
    link=usuarioA.link
    return render(request, 'AppUsuario/uprofile.html', {'imagen':imagen,'nusuario':nusuario,'nombre':nombre,'apellido':apellido,
    'email':email,'descripcion':descripcion,'link':link, 'user': user})


#Funcion para Obtener el Avatar
def getAvatar (request):
    avatar1= User.objects.get(username=request.user)
    avatar= AdditionalUser.objects.get(usuario=avatar1)
    imagen=avatar.imagen.url
    return (imagen)
        


