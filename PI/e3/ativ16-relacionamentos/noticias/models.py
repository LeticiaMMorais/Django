from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    titulo = models.CharField(max_length=300)
    texto = models.TextField()
    categoria = models.ForeignKey(
        Categoria,
        null=True,
        on_delete=models.SET_NULL,
        related_name = "noticia"
        )
    tag = models.ManyToManyField(
        Tag,
        related_name = "noticia",
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