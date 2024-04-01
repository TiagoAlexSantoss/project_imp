from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from apps.projectimp.views import cadastro, salvar, salvar_grupo, responder_item

urlpatterns = [
    path('', cadastro, name='cadastro'),
    path('salvar', salvar, name='salvar'),
    path('salvar_grupo', salvar_grupo, name='salvar_grupo'),
    path('responder_item/', responder_item, name='responder_item'),
]
