from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Categoria,
    Tag,
    Noticia,
    Perfil,
)
from .forms import *

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
    noticia = Noticia.objects.get(id=id)
    contexto = {
        'noticia':noticia,
    }
    return render(request, 'noticias/noticia-detalhe.html', contexto)

def noticia_criar(request):
    if request.method == "POST":
        form = NoticiaForm(request.POST)
        if form.is_valid():
            noticia = form.save()
            noticia.save()
            messages.success(request, "Notícia cadastrada com sucesso")
            return redirect('noticias:inicio')
    else: 
        form = NoticiaForm()
    return render(
        request, 
        'noticias/formularios/noticias-form.html', 
        {
            'form': form,
            'title_page': 'Criar nova notícia',
        },
    )

def noticia_editar(request, id):
    noticia = get_object_or_404(Noticia, id=id)

    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            messages.success(request, "Notícia atualizada com sucesso!")
            return redirect('noticias:noticia_detalhes', id)
    else:
        form = NoticiaForm(instance=noticia)

    return render(
        request,
        'noticias/formularios/noticias-form.html', 
        {
            'form': form,
            'title_page': 'Editar notícia',
        },
    )

def noticia_excluir(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    if request.method == 'POST':
        noticia.delete()
        messages.success(request, "Notícia excluída com sucesso")
    else:
        messages.error(request, "Ocorreu um erro. Não foi possível apagar a notícia.")
    return redirect('noticias:noticias')


# ------- Categorias -------
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

def categoria_criar(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            categoria.save()
            messages.success(request, "Categoria cadastrada com sucesso!")
            return redirect('noticias:categorias')
    else: 
        form = NoticiaForm()
    return render(
        request, 
        'noticias/formularios/categoria-form.html', 
        {
            'form': form,
            'title_page': 'Criar nova categoria',
        },
    )

def categoria_editar(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria atualizada com sucesso!")
            return redirect('noticias:categoria_detalhes', id)
    else:
        form = CategoriaForm(instance=categoria)

    return render(
        request,
        'noticias/formularios/categoria-form.html', 
        {
            'form': form,
            'title_page': 'Editar categoria',
        },
    )

def categoria_excluir(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        try: 
            categoria.delete()
            messages.success(request, "Categoria excluída com sucesso!")
        except ProtectedError:
            messages.error(request, "Não é possível excluir esta categoria, pois existem notícias vinculadas a ela.")
    return redirect('noticias:categorias')


# ------- Tags -------
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

def tag_criar(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save()
            tag.save()
            messages.success(request, "Tag cadastrada com sucesso!")
            return redirect('noticias:tags')
    else: 
        form = TagForm()
    return render(
        request, 
        'noticias/formularios/tag-form.html', 
        {
            'form': form,
            'title_page': 'Criar nova tag',
        },
    )

def tag_editar(request, id):
    tag = get_object_or_404(Tag, id=id)

    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag atualizada com sucesso!")
            return redirect('noticias:tag_detalhes', id)
    else:
        form = TagForm(instance=tag)

    return render(
        request,
        'noticias/formularios/tag-form.html', 
        {
            'form': form,
            'title_page': 'Editar tag',
        },
    )

def tag_excluir(request, id):
    tag = get_object_or_404(Tag, id=id)
    if request.method == 'POST':
        tag.delete()
        messages.success(request, "Tag excluída com sucesso!")
    else:
        messages.error(request, "Ocorreu um erro. Não foi possível apagar a tag.")
    return redirect('noticias:tags')