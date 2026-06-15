from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('cardapio/', views.menu_view, name='cardapio')
]