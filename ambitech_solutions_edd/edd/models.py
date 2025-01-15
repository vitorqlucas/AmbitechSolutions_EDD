from django.db import models
from django.contrib.auth.models import User

# Users (já criado pelo Django)

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cnpj_cpf = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_compra = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.email)
