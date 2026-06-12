from django.shortcuts import render
from contexto import return_context

def cardapio(request):
    return render(request, 'doces\cardapio.html', return_context())
