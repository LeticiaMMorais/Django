from django import forms
from django.forms import ModelForm
from .models import *

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields=["nome"]

        labels = {
            'nome':'Nome da categoria:',
        }

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["titulo"]

        labels = {
            'titulo':'Nome da tag:',
        }

        widgets = {
            "titulo": forms.TextInput(attrs={"class":"form-control"}),
        }


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["titulo", "texto", "categoria", "tag",]

        labels = {
            'titulo':'Manchete da notícia:', 
            'texto':'Conteúdo da notícia:', 
            'categoria':'Categoria associada:',
            'tag':'Tags associadas:',
        }

        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "texto": forms.Textarea(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "tag": forms.CheckboxSelectMultiple(attrs={"class": "form-checkbox"}),
        }

