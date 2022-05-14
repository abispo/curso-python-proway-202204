from django.views import generic
from ..models import Tag

# class-based views
# ou views genéricas


class IndexView(generic.ListView):
    model = Tag


    # O nome da variável de contexto será <nome_da_model> + '_list'
    # Nesse caso, o nome será 'tag_list'


class DetailView(generic.DetailView):
    model = Tag
