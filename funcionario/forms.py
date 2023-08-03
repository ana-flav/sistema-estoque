from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Funcionario
import re 

class FuncionarioForm(ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha novamente'}))
    
    class Meta:
        model = Funcionario
        fields = '__all__'
        

    def clean(self):
        cleaned_data = super().clean()  
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
    
        if re.search('[^/w]', password) is None:
            self.add_error('password', 'A senha deve ter pelo menos um caractere especial') 

        if len(password) < 8:
            self.add_error('password', 'A senha deve ter no mínimo 8 caracteres')

        if password and password2 and password != password2:
            self.add_error('password2', 'As senhas não são iguais')


        

        