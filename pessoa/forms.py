
from django import forms
from django.forms import fields, models
from .models import Pessoa

class PessoaForm(forms.ModelForm):

    data_nascimento = forms.DateField(  #Calendario
        widget = forms.TextInput(
            attrs = {"type": "date"}
        )
    )

    class Meta:
        model = Pessoa
        # quais campos vao ficar disponivel
        fields = ['nome_completo', 'data_nascimento', 'ativo'] #campo a campo - melhor controle
        # fields = ['__all__'] # todos