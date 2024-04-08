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
    
    tipos_por_item = {item.id: item.tipo for subgrupo, itens in itens_por_subgrupo.items() for item in itens}

    return render(request, 'resposta.html', {'subgrupos': subgrupos, 'itens_por_subgrupo': itens_por_subgrupo,  'tipos_por_item': tipos_por_item} )


def detalhes_grupo(request, grupo_id):
    grupo = CadastroGrupo.objects.get(pk=grupo_id, ativo=True)
    subgrupos = CadastroSubGrupo.objects.filter(nome_grupo=grupo, ativo=True)
    
    itens_por_subgrupo = {}
    
    # Iterar sobre os subgrupos ativos
    for subgrupo in subgrupos:
        # Filtrar itens ativos relacionados ao subgrupo
        itens_ativos = CadastroItem.objects.filter(nome_subgrupo=subgrupo, ativo=True)
        
        # Para cada item do tipo 'Lista', recupere as opções da lista
        for item in itens_ativos:
            if item.tipo == 'list':
                # Verifique se há uma lista associada ao item
                if item.lista:
                    # Recupere todas as opções da lista associada ao item
                    item.opcoes_lista = item.lista.opcaolista_set.all().order_by('ordem')
                    for opcao in item.opcoes_lista:
                        print(opcao.descricao, opcao.ordem)
        
        # Adicionar os itens ativos ao dicionário
        itens_por_subgrupo[subgrupo] = itens_ativos
    
    # Recuperar todos os grupos ativos ordenados pela ordem definida
    todos_grupos = CadastroGrupo.objects.filter(ativo=True).order_by('ordem_grupo')
    
    # Encontrar o índice do grupo atual na lista ordenada
    index_grupo_atual = list(todos_grupos).index(grupo)
    
    # Verificar se há um grupo anterior na lista
    if index_grupo_atual > 0:
        # Se houver um grupo anterior, obtenha o ID desse grupo
        grupo_anterior_id = todos_grupos[index_grupo_atual - 1].id
    else:
        # Caso contrário, defina o ID como None
        grupo_anterior_id = None
    
    # Verificar se há um próximo grupo na lista
    if index_grupo_atual < len(todos_grupos) - 1:
        # Se houver um próximo grupo, obtenha o ID desse grupo
        proximo_grupo_id = todos_grupos[index_grupo_atual + 1].id
    else:
        # Caso contrário, defina o ID como None
        proximo_grupo_id = None
    
    context = {
        'grupo': grupo,
        'subgrupos': subgrupos,
        'itens_por_subgrupo': itens_por_subgrupo,
        'grupo_anterior_id': grupo_anterior_id,  # Adicionando o grupo anterior ao contexto
        'proximo_grupo_id': proximo_grupo_id  # Adicionando o próximo grupo ao contexto
    }
    
    return render(request, 'detalhes_grupo.html', context)

