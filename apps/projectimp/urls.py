from django.urls import path
from apps.projectimp.views import cadastro, salvar,salvar_grupo, salvar_respostas
from django.conf import settings

urlpatterns = [
    path('', cadastro, name = 'cadastro'),
    path('salvar', salvar, name='salvar'),
    path('salvar_grupo', salvar_grupo, name='salvar_grupo'),
     path('salvar_respostas', salvar_respostas, name='salvar_respostas'),
]
