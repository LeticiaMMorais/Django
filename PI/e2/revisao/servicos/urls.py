from django.urls import path
from . import views

app_name = 'servicos'

urlpatterns = [
    path('lista/', views.lista_servicos, name='lista_servicos'),
    path('detalhes/<int:id_detalhe>/', views.detalhes_servicos, name='detalhes'),
]