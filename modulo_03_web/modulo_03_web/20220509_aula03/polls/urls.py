from django.urls import path

# Importamos o módulo 'views' que está no mesmo diretório de 'urls.py'
from . import views

# namespace
# Dessa maneira conseguimos diferenciar rotas que possuem o mesmo
# nome, porém que estão em pacotes diferentes
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote')
]
