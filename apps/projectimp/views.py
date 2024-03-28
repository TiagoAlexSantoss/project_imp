from django.shortcuts import render, redirect
from apps.projectimp.forms import IdentificacaoEmpresaForm, SalvarGrupoForm, SalvarRespostaForm
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


def salvar_respostas(request):
    if request.method == 'POST':
        form = SalvarRespostaForm(request.POST)
        if form.is_valid():
            form.save()
            # Aqui você pode adicionar uma mensagem de sucesso se desejar
            return redirect('salvar_respostas')  # Redirecione para uma página de sucesso após salvar
        else:
            # Se o formulário não for válido, você pode tratar os erros ou exibi-los na página
            # Por exemplo, você pode adicionar uma mensagem de erro aqui se desejar
            pass
    else:
        form = SalvarRespostaForm()
    
    return render(request, 'resposta.html', {'form': form})