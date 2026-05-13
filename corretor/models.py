from django.db import models
from usuarios.models import Aluno, Professor

class Exercicio(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    xml_base = models.TextField()

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo


class Submissao(models.Model):
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_submissao = models.DateTimeField(auto_now_add=True)
    xml_submetido = models.TextField()
    resultado = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-data_submissao']

    def __str__(self):
        return f'{self.aluno} → {self.exercicio}'


