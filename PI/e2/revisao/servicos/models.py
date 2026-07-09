from django.db import models

class Servico(models.Model):
    # Não coloquei id porque o Django já fez esse preenchimento de for automática
    nome_servico = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)
    tempo_estimado = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self):
        return self.nome_servico