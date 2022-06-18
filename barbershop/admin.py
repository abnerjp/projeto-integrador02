from django.contrib import admin

# Register your models here.


from .models import Servico

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    ...