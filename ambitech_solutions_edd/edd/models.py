from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Users (já criado pelo Django)

class Cliente(AbstractUser):
    cnpj_cpf = models.CharField(max_length=200)
    data_compra = models.DateField(null=True, blank=True)  # Permitir valores nulos
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.email)
