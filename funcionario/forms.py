from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Funcionario
from validate_docbr import CPF
import re 


cpf_validator = CPF()

class FuncionarioForm(ModelForm):
    
    class Meta:
        model = Funcionario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FuncionarioForm, self).__init__(*args, **kwargs)
        self.fields['user'].label = 'Usuário'


    def clean(self):
        cleaned_data = super().clean()  
        cpf = self.cleaned_data.get('cpf')
        email = self.cleaned_data.get('email')
    
        if cpf is not None and cpf!='':
            if not cpf_validator.validate(cpf):
                self.add_error('cpf', 'CPF inválido')
            
            if Funcionario.objects.filter(cpf=cpf).exists():
                self.add_error('cpf', 'CPF já cadastrado')
        
        if Funcionario.objects.filter(email=email).exists():
            self.add_error('email', 'E-mail já cadastrado')

        return cleaned_data
        
        

        

        