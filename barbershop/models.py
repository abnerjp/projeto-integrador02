from django.db import models
from datetime import time
# Create your models here.


class Cliente(models.Model):
    telefone_celular = models.CharField(max_length=14)
    nome = models.CharField(max_length=70)

    def __str__(self):
        return (f'{self.telefone_celular} | {self.nome}')


class Servico(models.Model):
    nome = models.CharField(max_length=70)
    tempo_estimado = models.TimeField(default=time(0, 30))
    descricao = models.CharField(max_length=200)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Agenda(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_agenda = models.DateTimeField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    confirmado = models.BooleanField(default=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT, null=False)
    servico = models.ForeignKey(Servico, on_delete=models.RESTRICT, null=False)

    def __str__(self):
        return (f'{self.data_agenda} | {self.hora_inicio} - {self.hora_fim} | {self.cliente} | ')