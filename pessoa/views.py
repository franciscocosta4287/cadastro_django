from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Pessoa

class ListaPessoaView(ListView):
    # quais registros listar
    model = Pessoa
    # qual query
    queryset: Pessoa.objects.all().order_by('nome_completo')
