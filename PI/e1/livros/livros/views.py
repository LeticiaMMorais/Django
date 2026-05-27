from django.shortcuts import render

def detalhe_livro_view(request):
    return render(request, 'livros/detalhe.html')

def lista_livro_view(request):
    return render(request, 'livros/lista.html')
