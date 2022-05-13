from django.shortcuts import render

from ..models import Comment


def index(request):

    comments_list = Comment.objects.all()

    context = {
        'comments_list': comments_list
    }

    return render(request, 'comments/index.html', context=context)


def detail(request, comment_id):
    pass
