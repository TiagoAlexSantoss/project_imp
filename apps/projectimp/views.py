from audioop import reverse
from django.shortcuts import render, redirect, get_object_or_404
from apps.projectimp.forms import IdentificacaoEmpresaForm, SalvarGrupoForm, CadastroRespostaItemForm
from apps.projectimp.models import CadastroItem, CadastroSubGrupo, CadastroGrupo, CadastroRespostaItem
from django.contrib import messages
from django.http import HttpResponse, JsonResponse

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
    
    tipos_por_item = {item.id: item.tipo for subgrupo, itens in itens_por_subgrupo.items() for item in itens}

    return render(request, 'resposta.html', {'subgrupos': subgrupos, 'itens_por_subgrupo': itens_por_subgrupo,  'tipos_por_item': tipos_por_item} )

def detalhes_grupo(request, grupo_id):

    if request.method == 'POST':
        grupo_atual = CadastroGrupo.objects.get(pk=grupo_id, ativo=True)
        subgrupos = CadastroSubGrupo.objects.filter(nome_grupo=grupo_atual, ativo=True)
        for subgrupo in subgrupos:
            itens_ativos = CadastroItem.objects.filter(nome_subgrupo=subgrupo, ativo=True)
            for item in itens_ativos:
                resposta = request.POST.get(item.nome_item)
                CadastroRespostaItem.objects.create(resposta_item=resposta, nome_item=item)
        
        proximo_grupo = CadastroGrupo.objects.filter(ativo=True, ordem_grupo__gt=grupo_atual.ordem_grupo).order_by('ordem_grupo').first()
        if proximo_grupo:
            # Redireciona para a próxima página após salvar os dados
            return redirect('detalhes_grupo', grupo_id=proximo_grupo.id)
        else:
            return HttpResponse("Processamento concluído. Não há próximo grupo.")

    grupo = CadastroGrupo.objects.get(pk=grupo_id, ativo=True)
    subgrupos = CadastroSubGrupo.objects.filter(nome_grupo=grupo, ativo=True)
    itens_por_subgrupo = {}
    for subgrupo in subgrupos:
        itens_ativos = CadastroItem.objects.filter(nome_subgrupo=subgrupo, ativo=True)
        for item in itens_ativos:
            if item.tipo == 'list':
                if item.lista:
                    item.opcoes_lista = item.lista.opcaolista_set.all().order_by('ordem')
        itens_por_subgrupo[subgrupo] = itens_ativos
    
    todos_grupos = CadastroGrupo.objects.filter(ativo=True).order_by('ordem_grupo')
    index_grupo_atual = list(todos_grupos).index(grupo)
    
    grupo_anterior_id = None
    proximo_grupo_id = None
    
    if index_grupo_atual > 0:
        grupo_anterior_id = todos_grupos[index_grupo_atual - 1].id
    
    if index_grupo_atual < len(todos_grupos) - 1:
        proximo_grupo_id = todos_grupos[index_grupo_atual + 1].id
    
    context = {
        'grupo': grupo,
        'subgrupos': subgrupos,
        'itens_por_subgrupo': itens_por_subgrupo,
        'grupo_anterior_id': grupo_anterior_id,
        'proximo_grupo_id': proximo_grupo_id
    }
    
    return render(request, 'detalhes_grupo.html', context)

def crud_resposta_item(request):
    if request.method == 'POST':
        form = CadastroRespostaItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nova_view')
    else:
        form = CadastroRespostaItemForm()
    
    subgrupos = CadastroSubGrupo.objects.all()
    
    itens_por_subgrupo = {}
    for subgrupo in subgrupos:
        itens_ativos = CadastroItem.objects.filter(nome_subgrupo=subgrupo, ativo=True)
        itens_por_subgrupo[subgrupo] = itens_ativos
    
    context = {
        'itens_por_subgrupo': itens_por_subgrupo,
        'form': form
    }
    
    return render(request, 'crud_resposta_item.html', context)