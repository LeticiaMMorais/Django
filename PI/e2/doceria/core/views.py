import os
from django.shortcuts import render
from django.http import HttpResponse

#arquivo_contexto = os.path.normpath('../contexto.py')
import contexto

def resposta_view(request):
    print("Request:", request)
    print('Método:', request.method)
    print('GET:', request.GET)
    print("Caminho: ", request.path)
    print('Usuário:', request.user)
    return HttpResponse("Esta é a minha view!")

def home(request):
    return render(request, 'index.html', contexto.return_context())

def sobre_nos(request):
    return render(request, 'sobre.html', contexto.return_context())
