from django.urls import path

# Importamos o módulo 'views' que está no mesmo diretório de 'urls.py'
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
