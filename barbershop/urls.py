from django.urls import path

from . import views

app_name = 'barbershop'
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.home, name='administracao'),
    path('galeria/', views.galeria, name='galeria'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('agenda/', views.agendamento, name='agendamento'),
    path('agenda/inicio/', views.inicio_agendamento, name='inicio_agendamento'),
    path('agenda/consulta/', views.consulta_agenda, name='consulta_agenda'),
    path('valida_agendamento/', views.pre_agendamento, name='pre_agendamento'),
    path('agenda/criacao/', views.confirmar_agendamento, name='confirmacao'),
    path('agenda/enviado/', views.fim_agendamento, name='fim_agendamento'),
    path('agenda/confirmacao/', views.ver_agenda, name='ver_registros_agenda'),
    path('agenda/confirmacao/<uuid:codigo_uuid>/', views.validar_agenda, name='confirmacao_registro'),
    path('agenda/confirmacao/agenda', views.confirmacao_agenda_pelo_dono, name='confirmacao_final_agenda'),
]

