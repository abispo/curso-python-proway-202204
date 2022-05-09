from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse

from .models import Question


# Function based views
# Class based views

# Precisam receber o argumento request
def index(request):
    # Pegamos a lista das 5 perguntas mais recenter
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # Question.objects.get(pk=question_id)

    # Criamos o dicionário que será passado na renderização do template
    context = {
        'latest_question_list': latest_question_list
    }

    return render(request, 'polls/index.html', context=context)


def detail(request, question_id):
    # Pegar o question_id passado na url
    # Usar esse question_id pra fazer a consulta no banco, retornando a questão correspondente

    # Retorne da tabela de questions um valor cuja a chave primária (pk) seja
    # igual a question_id
    question = get_object_or_404(Question, pk=question_id)

    # Criar um dicionário que será passado como contexto na função render
    context = {
        'question': question
    }

    # No template exibir o question_text dentro de uma tag <h1>
    return render(request, 'polls/detail.html', context=context)


def results(request, question_id):
    return HttpResponse(f"Você está olhando os resultados da pergunta {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"Você está votando na pergunta {question_id}.")
