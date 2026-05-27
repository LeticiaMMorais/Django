from django.urls import path
from . import views

app_name = 'livros'

urlpatterns = [
    path('detalhe/', views.detalhe_livro_view, name='detalhe'),
    path('lista/', views.lista_livro_view, name='lista'),
]