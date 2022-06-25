from django.db import models
from datetime import *
import uuid
import re

# Create your models here.


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
    nome_cliente = models.CharField(max_length=70, null=False)
    codigo_uuid = models.CharField(max_length=36, null=False, default=str(uuid.uuid4()))
    celular_cliente = models.CharField(max_length=14, null=False)
    observacao_cliente = models.CharField(max_length=150, null=True)
    servico = models.ForeignKey(Servico, on_delete=models.RESTRICT, null=False)


    def __str__(self):
        confirmado = " | Confirmado" if self.data_hora_confirmacao is not None else ""
        return (
            f'Agenda: {self.data_hora_inicio} - {self.data_hora_fim} | Cliente: {self.nome_cliente}{confirmado}')