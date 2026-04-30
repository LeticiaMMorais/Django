from django.contrib import admin
from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('detalhes/', views.detalhes, name='detalhes'),
    path("admin/", admin.site.urls),
]