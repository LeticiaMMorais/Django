from django.shortcuts import render

def lista(request):
    return render(request, 'produtos/lista.html')

def detalhes(request):
    return render(request, 'produtos/detalhes.html')