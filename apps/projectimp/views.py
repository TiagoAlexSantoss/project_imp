from django.shortcuts import render, redirect
from apps.projectimp.forms import IdentificacaoEmpresaForm, SalvarGrupoForm
from django.contrib import messages

def cadastro(request): 
    return render(request, 'cadastro.html')

def salvar(request):
    if request.method == 'POST':
        form = IdentificacaoEmpresaForm(request.POST)
        if form.is_valid():  
            form.save()
            messages.success(request, 'Salvo com sucesso')
            return redirect('cadastro')
        else:
            # Imprimir os erros de validação para entender o motivo da falha
            print(form.errors)
            messages.error(request, 'Erro ao salvar. Verifique os dados.')
    else:
        form = IdentificacaoEmpresaForm()
    
    return render(request, 'cadastro.html', {'form': form})

def salvar_grupo(request):
    if request.method == 'POST':
        form = SalvarGrupoForm(request.POST)
        if form.is_valid():  
            form.save()
            messages.success(request, 'Salvo com sucesso')
            return redirect('salvar_grupo')
        else:
            # Imprimir os erros de validação para entender o motivo da falha
            print(form.errors)
            messages.error(request, 'Erro ao salvar. Verifique os dados.')
    else:
        form = SalvarGrupoForm()
    
    return render(request, 'cadastro_grupo.html', {'form': form})
