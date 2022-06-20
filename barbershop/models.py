from django.db import models
from datetime import time, datetime
# Create your models here.


class Cliente(models.Model):
    data_hora_criacao = models.DateTimeField(auto_now_add=True)
    telefone_celular = models.CharField(max_length=14)
    nome = models.CharField(max_length=70)
    data_hora_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f'{self.telefone_celular} | {self.nome}')


class Servico(models.Model):
    nome = models.CharField(max_length=70)
    descricao = models.CharField(max_length=200)
    tempo_estimado = models.TimeField(default=time(0, 30))
    ativo = models.BooleanField(default=True)
    data_hora_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Agenda(models.Model):
    data_hora_criacao = models.DateTimeField(auto_now_add=True)
    data_hora_inicio = models.DateTimeField()
    data_hora_fim = models.DateTimeField()
    data_hora_confirmacao = models.DateTimeField(null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT, null=False)
    servico = models.ForeignKey(Servico, on_delete=models.RESTRICT, null=False)

    def __str__(self):
        return (f'Agenda: {self.data_hora_inicio} - {self.data_hora_fim} | {self.cliente} | Confirmado {self.data_hora_confirmacao}')