
from django.http import HttpResponse


def index(request):
    return HttpResponse("Curso de Python da Proway")
