from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView
from .models import Pessoa
from .forms import PessoaForm

class ListaPessoaView(ListView):
    # quais registros listar
    model = Pessoa
    # qual query
    queryset: Pessoa.objects.all().order_by('nome_completo')


class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    # url de sucesso
    success_url = '/pessoas/'
