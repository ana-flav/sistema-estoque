from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .models import Funcionario
from .forms import FuncionarioForm

class FuncionarioCreate(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'funcionario_tela_cadastro.html'
    success_url = reverse_lazy('funcionario:login')


class FuncionarioLoginView(LoginView):
    model = Funcionario
    template_name = 'funcionario_tela_login.html'