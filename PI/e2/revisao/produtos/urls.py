from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('lista/', views.lista_produtos, name='lista_produtos'),
    path('detalhes/<int:id_detalhes>/', views.detalhes_produtos, name='detalhes'),
]