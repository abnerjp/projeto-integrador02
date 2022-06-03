from django.urls import path

from . import views

app_name = 'barbershop'

urlpatterns = [
    path('', views.home, name='home'),
    path('galeria/', views.galeria, name='galeria'),
    path('catalogo/', views.catalogo, name='catalogo'),
]
