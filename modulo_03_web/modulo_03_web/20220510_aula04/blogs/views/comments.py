from django.shortcuts import render, get_object_or_404

from ..models import Comment


def index(request):

    comments_list = Comment.objects.all()

    context = {
        'comments_list': comments_list
    }

    return render(request, 'comments/index.html', context=context)


def detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    # Criar um dicionário que será passado como contexto na função render
    context = {
        'comment': comment
    }

    # No template exibir o question_text dentro de uma tag <h1>
    return render(request, 'comments/detail.html', context=context)
