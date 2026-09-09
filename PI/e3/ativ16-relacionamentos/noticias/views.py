from django.shortcuts import render
from .models import (
    Categoria,
    Tag,
    Noticia,
    Perfil,
)

def inicio(request):
    noticias = Noticia.objects.order_by('-id')[:3]
    contexto = {
        'noticias':noticias,
    }
    return render(request, 'noticias/index.html', contexto)

def noticias(request):
    noticias = Noticia.objects.all()
    contexto = {
        'noticias':noticias,
    }
    return render(request, 'noticias/noticias.html', contexto)

def noticia_detalhes(request, id):
    noticia = noticia.objects.get(id=id)
    contexto = {
        'noticia':noticia,
    }
    return render(request, 'noticias/noticia-detalhe.html', contexto)

def categorias(request):
    categorias = Categoria.objects.all()
    contexto = {
        'categorias':categorias,
    }
    return render(request, 'noticias/categorias.html', contexto)

def categoria_detalhes(request,id):
    categoria = Categoria.objects.get(id=id)
    contexto = {
        'categoria':categoria,
    }
    return render(request, 'noticias/categoria-detalhe.html', contexto)

def tags(request):
    tags = Tag.objects.all()
    contexto = {
        'tags':tags,
    }
    return render(request, 'noticias/tags.html', contexto)

def tag_detalhes(request,id):
    tag = Tag.objects.get(id=id)
    contexto = {
        'tag':tag,
    }
    return render(request, 'noticias/tag-detalhe.html', contexto)