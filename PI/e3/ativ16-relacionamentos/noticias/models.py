from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    titulo = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    titulo = models.CharField(max_length=300, blank=False)
    texto = models.TextField(blank=False)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name = "noticia"
        )
    tag = models.ManyToManyField(
        Tag,
        related_name = "noticia",
        null=True,
    )


    def __str__(self):
        return f'{self.titulo} - {self.categoria}'


class Perfil(models.Model):
    bio = models.TextField()
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name = "perfil"
    )

    def __str__(self):
        return self.usuario.username