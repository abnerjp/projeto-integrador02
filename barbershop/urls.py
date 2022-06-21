from django.urls import path

from . import views

app_name = 'barbershop'

urlpatterns = [
    path('', views.home, name='home'),
    path('galeria/', views.galeria, name='galeria'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('inicio-agendamento/', views.inicio_agendamento, name='inicio_agendamento'),
    path('consulta-agenda/', views.consulta_agenda, name='consulta_agenda'),
    path('valida_agendamento/', views.pre_agendamento, name='pre_agendamento'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('agendamento/confirmacao/', views.confirmar_agendamento, name='confirmacao'),
    path('agendamento/enviado/', views.fim_agendamento, name='fim_agendamento'),
]
