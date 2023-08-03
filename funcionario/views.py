from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Funcionario
from .forms import FuncionarioForm

class FuncionarioCreate(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'funcionario_tela_cadastro.html'