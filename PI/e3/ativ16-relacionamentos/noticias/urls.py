from django.urls import path, include
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.inicio, name='inicio'),

    #  Noticias
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/<int:id>/', views.noticia_detalhes, name='noticia_detalhes'),
    path('noticias/criar/', views.noticia_criar, name="noticia_criar"),
    path('noticias/editar/<int:id>/', views.noticia_editar, name='noticia_editar'),
    path('noticias/excluir/<int:id>/', views.noticia_excluir, name='noticia_excluir'),

    # Categorias
    path('noticias/categorias/', views.categorias, name='categorias' ),
    path('noticias/categorias/<int:id>/', views.categoria_detalhes, name='categoria_detalhes'),
    path('noticias/categorias/criar/', views.categoria_criar, name="categoria_criar"),
        path('noticias/categorias/editar/<int:id>/', views.categoria_editar, name='categoria_editar'),
        path('noticias/categorias/excluir/<int:id>/', views.categoria_excluir, name='categoria_excluir'),

    # Tags
    path('noticias/tags/', views.tags, name='tags'),
    path('noticias/tags/<int:id>/', views.tag_detalhes, name='tag_detalhes'),
    path('noticias/tags/criar/', views.tag_criar, name="tag_criar"),
    path('noticias/tags/editar/<int:id>/', views.tag_editar, name='tag_editar'),
    path('noticias/tags/excluir/<int:id>/', views.tag_excluir, name='tag_excluir'),
]