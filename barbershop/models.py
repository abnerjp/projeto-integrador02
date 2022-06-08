from django.db import models
# api rnbfX6q4TXQW5T4T41B7-OfhVXUgyJEbfUI5hffn
# Create your models here.

class Agendamento(models.Model):
    nome = models.CharField(max_length=70)
    telefone_celular = models.CharField(max_length=14)
    data_hora_cadastro = models.DateTimeField(auto_now_add=True)
    data_hora_agenda = models.DateTimeField()
    observacao = models.CharField(max_length=150)
    slug = models.SlugField()
