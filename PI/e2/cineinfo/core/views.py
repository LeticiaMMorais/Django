from django.shortcuts import render

from . import models

def home(resquest):
    filmes = models.Filme.objects.all()
    contexto = {
        'filmes': filmes,
    }
    return render(resquest, 'index.html', context=contexto)