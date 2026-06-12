from django.urls import path
from . import views

app_name = 'doces'

urlpatterns =[
    path('cardapio/', views.cardapio, name='cardapio')
]