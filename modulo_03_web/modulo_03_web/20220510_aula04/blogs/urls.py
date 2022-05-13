from django.urls import path

# Importamos o módulo 'views' que está no mesmo diretório de 'urls.py'
from .views import posts, comments

# namespace
# Dessa maneira conseguimos diferenciar rotas que possuem o mesmo
# nome, porém que estão em pacotes diferentes
app_name = 'blogs'

urlpatterns = [
    # posts
    path('posts/', posts.index, name='index'),
    path('posts/<int:post_id>/', posts.detail, name='detail'),

    #comments
    path('comments/', comments.index, name='index_comments'),
    path('comments/<int:comment_id>/', comments.detail, name='detail_comments'),
]
