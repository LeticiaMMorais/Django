from django.urls import path, include
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('lista_disciplinas', views.lista_disciplinas, name='lista_disciplinas'),
    path('autorizacao', views.autorizacao, name='autorizacao'),
    path('biblioteca', views.biblioteca, name='biblioteca'),
    path('prioridade', views.prioridade, name='prioridade'),
    path('lista_alunos', views.lista_alunos, name='lista_alunos'),
    path('detalhes/<int:livro_id>/', views.detalhes,name='detalhes_livro'),
    path('alerta', views.alerta, name='alerta')
]