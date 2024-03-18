from django.urls import path
from apps.projectimp.views import cadastro

urlpatterns = [
    path('', cadastro),
]