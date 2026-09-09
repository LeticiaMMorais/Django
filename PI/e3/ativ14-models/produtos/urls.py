from django.urls import path, include
from . import views

app_name = 'produtos'

urlpatterns = [
    path('listaProdutos/', views.listagem, name='listaProdutos'),
    path('detalhesProduto/<int:id>/', views.detalhes, name='detalhesProduto'),
]
