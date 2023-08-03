from django.db import models
from django.contrib.auth.models import User


CHOICES_CARGOS = ((1, 'Administrador'), (1, 'Gerente'), (3, 'Funcionário'))

class Funcionario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário', null=True,
        blank=True)
    cpf = models.CharField("CPF", max_length=11, blank=True, null=True, unique=True)
    nome = models.CharField("Nome", max_length=300)
    email = models.EmailField("E-mail", unique=True)
    cargo = models.IntegerField("Cargo", choices= CHOICES_CARGOS)
    cod_trabalhador = models.IntegerField("Código do Trabalhador", blank=True, null=True)