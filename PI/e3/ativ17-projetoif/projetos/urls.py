from django.urls import path
from . import views

app_name = 'projetos'

urlpatterns = [
    path('', views.listagem_view, name='listagem-projetos'),
    path('projeto/<int:id>/', views.detalhesProjeto_view, name='detalhes-projeto'),
    path('aluno/<int:id>/', views.detalhesAluno_view, name='detalhes-aluno'),
]