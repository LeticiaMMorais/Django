from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    contexto = {
        'produtos':produtos,
    }
    return render(request, 'produtos/produtos.html', context=contexto)

def detalhes_produtos(request, id_detalhes):
    produto = Produto.objects.get(id=id_detalhes)
    contexto = {
        'produto':produto,
    }
    return render(request, 'produtos/detalhes.html', context=contexto)