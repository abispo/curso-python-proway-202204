
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accounts.models import Account, Transaction


def index(request):
    # Como pegar o user?
    # request.user -> Usuário atualmente logado
    total_num_accounts = request.user.account_set.all().count()
    # Transaction => Account => User
    # Dessa maneira, conseguirmos pegar todas as transações onde:
    # A conta de débito pertence ao usuário que está armazenado em
    # request.user
    total_num_transactions = Transaction.objects.filter(debit_account__user=request.user).count()

    context = {
        'total_num_accounts': total_num_accounts,
        'total_num_transactions': total_num_transactions
    }

    return render(request, 'users/index.html', context=context)


def detail(request: HttpRequest, user_id: int) -> HttpResponse:

    return render(request, 'users/detail.html')


def create_account(request):

    if request.method == 'GET':
        return render(request, 'accounts/create.html')

    elif request.method == 'POST':

        post_data = request.POST

        if len(post_data.get("txtInitialBalance").strip()):
            balance = float(post_data.get("txtInitialBalance").strip())
        else:
            balance = 0

        account = Account(
            user=request.user,
            name=post_data.get("txtAccountName"),
            balance=balance
        )

        account.save()

        # reverse() converte um padrão de nome de rota para uma URL
        # Por exemplo, a linha abaixo reverse('users:list_accounts',))
        # Será convertida para a URL http://127.0.0.1:8000/users/me/accounts
        return HttpResponseRedirect(reverse('users:list_accounts',))


def list_accounts(request):

    # Pega todas as contas associadas ao usuário logado
    user_accounts = request.user.account_set.all()

    context = {
        'user_accounts': user_accounts
    }

    return render(request, 'accounts/list.html', context=context)


def create_transaction(request):
    return render(request, 'transactions/create.html')
