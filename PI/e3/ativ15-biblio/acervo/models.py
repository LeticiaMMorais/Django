from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    ano_nascimento = models.IntegerField(validators=[MaxValueValidator(2026)])

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    data_lancamento = models.DateField()
    autor = models.ForeignKey(
        Autor,
        on_delete=models.PROTECT,
        null=True,
    )
    resumo = models.TextField(max_length=1500, null=True)
    editora = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo}  -  {self.autor}"
