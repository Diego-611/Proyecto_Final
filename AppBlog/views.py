from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AppUsuario.views import getAvatar
from .models import Blog


#Vista de Inicio
def viewIndex (request):
    blog=Blog.objects.all().order_by('-fecha')
    return render(request, 'AppBlog/index.html', {'blogs':blog})

#Vista de Inicio
@login_required
def viewRIndex (request):
    blog=Blog.objects.all()
    return render(request, 'AppBlog/rindex.html', {'imagen': getAvatar(request), 'blogs':blog})

#Vista de Cada Blog
@login_required
def viewBlog (request, id):
    pagina=Blog.objects.get(id=id)
    autor=pagina.autor
    titulo=pagina.titulo
    subtitulo=pagina.subtitulo
    cuerpo=pagina.cuerpo
    imagen=pagina.imagen.url
    fecha=pagina.fecha
    return render(request, 'AppBlog/page.html', {'autor':autor,'titulo': titulo,'subtitulo': subtitulo,
    'cuerpo':cuerpo,'imagen':imagen,'fecha':fecha})

#Vista de Los Creadores
@login_required
def viewAbout(request):
    return render(request, 'AppBlog/about.html')



