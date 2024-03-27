from django.urls import path
from apps.projectimp.views import cadastro, salvar,salvar_grupo
from django.conf import settings

urlpatterns = [
    path('', cadastro, name = 'cadastro'),
    path('salvar', salvar, name='salvar'),
    path('salvar_grupo', salvar_grupo, name='salvar_grupo'),
]
