from django.contrib import admin

# Register your models here.


from .models import Servico, Cliente, Agenda

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    ...

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    ...

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    ...