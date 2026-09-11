from django.contrib import admin
from .models import (
    Categoria,
    Aluno,
    PerfilAcademico,
    Projeto,
)


class AlunoAdmin(admin.ModelAdmin):
    list_display=['nome','matricula']
    search_display=['nome','matricula']
    ordering = ['nome']


admin.site.register(Categoria)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(PerfilAcademico)
admin.site.register(Projeto)
