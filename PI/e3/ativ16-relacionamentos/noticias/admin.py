from django.contrib import admin
from .models import (
    Categoria,
    Tag,
    Noticia,
    Perfil,
)

class NoticiaAdmin(admin.ModelAdmin):
    search_fields = ("titulo","categoria","tag")
    list_filter = ("categoria", "tag")

admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Perfil)