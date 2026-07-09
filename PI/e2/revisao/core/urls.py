from django.urls import path, include
from . import views

app_name = ''

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', include('produtos.urls', namespace='produtos')),
    path('servicos/', include('servicos.urls', namespace='servicos'))
]