from django.urls import path, include
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/<int:id>/', views.noticia_detalhes, name='noticia_detalhes'),
    path('noticias/categorias/', views.categorias, name='categorias' ),
    path('noticias/categorias/<int:id>/', views.categoria_detalhes, name='categoria_detalhes'),
    path('noticias/tags/', views.tags, name='tags'),
    path('noticias/tags/<int:id>/', views.tag_detalhes, name='tag_detalhes'),
]