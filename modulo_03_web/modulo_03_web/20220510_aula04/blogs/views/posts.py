from django.http import Http404
from django.shortcuts import render, get_object_or_404

from ..models import Post

# Listar todos os posts
def index(request):

    # SELECT * FROM blogs_post
    posts = Post.objects.all()

    context = {
        'post_list': posts
    }

    # Renderiza o template
    return render(request, 'posts/tag_list.html', context=context)


# Entrar no detalhe de um post
def detail(request, post_id):
    # Pegar o question_id passado na url
    # Usar esse question_id pra fazer a consulta no banco, retornando a questão correspondente

    # Retorne da tabela de questions um valor cuja a chave primária (pk) seja
    # igual a question_id
    # SELECT * FROM blogs_post WHERE id = :post_id
    post = get_object_or_404(Post, pk=post_id)


    # Criar um dicionário que será passado como contexto na função render
    context = {
        'post': post
    }

    # No template exibir o question_text dentro de uma tag <h1>
    return render(request, 'posts/tag_detail.html', context=context)
