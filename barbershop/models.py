from django.db import models
# Create your models here.


class Cliente(models.Model):
    telefone_celular = models.CharField(max_length=14)
    nome = models.CharField(max_length=70)

class Servico(models.Model):
    nome = models.CharField(max_length=70)
    descricao = models.CharField(max_length=200)


class Agenda(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_agenda = models.DateTimeField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    confirmado = models.BooleanField(default=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=False)
