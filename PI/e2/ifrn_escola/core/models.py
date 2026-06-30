from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=120)
    matricula = models.CharField(max_length=10) 

    def __str__(self):
        return f"{self.nome} ({self.matricula})"
    
    def get_nome (self):
        return self.nome
    
    def get_matricula(self):
        return self.matricula
    
    
class Livro(models.Model):
    titulo = models.CharField(max_length=250)
    autor = models.CharField(max_length=250)
    ano = models.IntegerField()
    sinopse = models.TextField()

    def __str__(self):
        return f"{self.titulo}"
    
