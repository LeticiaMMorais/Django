from django.shortcuts import render
from .models import Servico

def lista_servicos(request):
    servicos = Servico.objects.all()
    contexto = {
        'servicos':servicos,
    }
    return render(request, 'servicos/servicos.html', context=contexto)

def detalhes_servicos(request, id_detalhe):
    servico = Servico.objects.get(id=id_detalhe)
    contexto = {
        'servico':servico,
    }
    return render(request, 'servicos/detalhes.html', context=contexto)