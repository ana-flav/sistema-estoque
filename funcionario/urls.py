from django.urls import path
from .views import FuncionarioCreate, FuncionarioLoginView

app_name = 'funcionario'

urlpatterns = [
    path('cadastro/', FuncionarioCreate.as_view(), name='cadastro'),    
    path('login/', FuncionarioLoginView.as_view(), name='login'),    
]