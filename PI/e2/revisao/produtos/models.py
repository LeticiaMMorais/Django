from django.db import models

class Produto(models.Model):
    # Não estou colocando ID porque já será automático
    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    preco = models.FloatField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome