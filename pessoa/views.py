from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pessoa
from .forms import PessoaForm

class ListaPessoaView(ListView):
    # quais registros listar
    model = Pessoa
    # qual query
    queryset: Pessoa.objects.all().order_by('nome_completo')

    # filtro
    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)
        return queryset



class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    # url de sucesso
    success_url = '/pessoas/'

class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'

class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/pessoas/'