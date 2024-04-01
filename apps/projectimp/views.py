from django.shortcuts import render, redirect, get_object_or_404
from apps.projectimp.forms import IdentificacaoEmpresaForm, SalvarGrupoForm
from apps.projectimp.models import CadastroItem, CadastroSubGrupo, CadastroGrupo
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


def responder_item(request):
    subgrupos = CadastroSubGrupo.objects.order_by('ordem_subgrupo').all()

    itens_por_subgrupo = {}
    
    for subgrupo in subgrupos:
        itens_por_subgrupo[subgrupo] = CadastroItem.objects.filter(nome_subgrupo=subgrupo)
    return render(request, 'resposta.html', {'subgrupos': subgrupos, 'itens_por_subgrupo': itens_por_subgrupo})
    