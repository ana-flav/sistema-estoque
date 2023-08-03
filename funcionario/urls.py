from django.urls import path
from .views import FuncionarioCreate

app_name = 'funcionario'

urlpatterns = [
    path('cadastro/', FuncionarioCreate.as_view(), name='cadastro'),    
]