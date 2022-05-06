from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Function based views
# Class based views

# Precisam receber o argumento request
def index(request):
    # Pegamos a lista das 5 perguntas mais recenter
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # Criamos o dicionário que será passado na renderização do template
    context = {
        'latest_question_list': latest_question_list
    }

    return render(request, 'polls/index.html', context=context)


def detail(request, question_id):
    return HttpResponse(f"Você está olhando os detalhes da pergunta {question_id}.")


def results(request, question_id):
    return HttpResponse(f"Você está olhando os resultados da pergunta {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"Você está votando na pergunta {question_id}.")
