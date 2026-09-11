from django.shortcuts import render
from . import models

def listagem_view(resquest):
    projetos = models.Projeto.objects.all()
    categorias = models.Categoria.objects.all()
    return render(
        resquest, 
        'projetos/listagem-projetos.html', 
        {'projetos':projetos, 'categorias':categorias},
    )

def detalhesProjeto_view(request, id):
    projeto = models.Projeto.objects.get(id=id)
    return render(
        request,
        'projetos/detalhes-projeto.html',
        {'projeto':projeto},
    )

def detalhesAluno_view(request, id):
    aluno = models.Aluno.objects.get(id=id)
    perfil = models.PerfilAcademico.objects.get(aluno_id=id)
    return render(
        request,
        'projetos/detalhes-aluno.html',
        {'aluno':aluno,'perfil':perfil},
    )