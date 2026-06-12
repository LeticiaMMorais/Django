from django.urls import path, include
from . import views

app_name = "core"

urlpatterns = [
    path('resposta/', views.resposta_view, name="resposta"),
    path('', views.home, name='home'),
    path('sobre/',views.sobre_nos, name='sobre_nos'),
    
]