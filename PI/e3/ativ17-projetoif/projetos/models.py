from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=80)
    matricula = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.nome}'


class PerfilAcademico(models.Model):
    link_lattes = models.URLField(
        blank=True,
        null=True,
    )
    biografia = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
    )
    aluno = models.OneToOneField(
        Aluno,
        on_delete=models.CASCADE,
        null=False,
        related_name='perfilacademico',
    )

    def __str__(self):
        return self.aluno.nome


class Projeto(models.Model):
    titulo = models.CharField(
        max_length=300, 
        null=False,
    )
    descricao = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
    )
    data_inicio = models.DateField(
        blank=True,
        null=True,
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='projeto',
    )
    equipe = models.ManyToManyField(
        Aluno,
        related_name='projeto',
    )

    def __str__(self):
        return self.titulo
