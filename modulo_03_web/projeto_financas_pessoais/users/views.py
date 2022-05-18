
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render


def index(request):

    return render(request, 'users/index.html')


def detail(request: HttpRequest, user_id: int) -> HttpResponse:

    return render(request, 'users/detail.html')
