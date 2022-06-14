from django.db import models

# Create your models here.
class Pessoa(models.Model):
    # nome_completo = models.CharField(max_length=256, null=True, blank=True), #naão obrigatorio
    nome_completo = models.CharField(max_length=256) # Obrigatório
    data_nascimento = models.DateField(null=True)
    ativo = models.BooleanField(default=True)
