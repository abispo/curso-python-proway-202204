
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request):
    # Como pegar o user?
    # request.user -> Usuário atualmente logado
    total_num_accounts = request.user.account_set.all().count()

    context = {
        'total_num_accounts': total_num_accounts
    }

    return render(request, 'users/index.html', context=context)


def detail(request: HttpRequest, user_id: int) -> HttpResponse:

    return render(request, 'users/detail.html')
