from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    lote = models.CharField(max_length=5)

    def __str__(self):
        return self.nome