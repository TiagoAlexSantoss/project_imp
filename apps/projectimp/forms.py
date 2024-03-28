from django import forms
from apps.projectimp.models import IdentificacaoEmpresa, CadastroGrupo, CadastroRespostaItem

class IdentificacaoEmpresaForm(forms.ModelForm):
    class Meta:
        model = IdentificacaoEmpresa
        fields = ['nome_empresa', 'email_empresa', 'fone_empresa', 'cnpj_empresa']
        labels = {
            'nome_empresa': 'Nome da Empresa',
            'cnpj_empresa': 'CNPJ',
            'email_empresa': 'E-mail',
            'fone_empresa': 'Fone/Whats',
                }

        widgets = {
            'nome_empresa': forms.TextInput(attrs={'class':'form-control'}),
            'cnpj_empresa': forms.TextInput(attrs={'class':'form-control'}),
            'email_empresa': forms.TextInput(attrs={'class':'form-control'}),            
            'fone_empresa': forms.TextInput(attrs={'class':'form-control'}),
            }
        
class SalvarGrupoForm(forms.ModelForm):
    class Meta:
        model = CadastroGrupo
        fields = ['nome_grupo', 'ordem_grupo', 'ativo']
        labels = {
            'nome_grupo': 'Nome do Grupo',
            'ordem_grupo': 'Ordem Grupo',
            'ativo': 'Ativo',
                }

        widgets = {
            'nome_grupo': forms.TextInput(attrs={'class':'form-control'}),
            'ordem_grupo': forms.NumberInput(attrs={'class':'form-control'}),
            'ativo': forms.CheckboxInput(),            
            }
        
class SalvarRespostaForm(forms.ModelForm):
    class Meta:
        model = CadastroRespostaItem
        fields = ['nome_item', 'resposta_item']

        widgets = {
            'nome_item': forms.TextInput(attrs={'class':'form-control', 'readonly': True}),  # Defina como somente leitura para evitar edição
            'resposta_item': forms.TextInput(attrs={'class':'form-control'}),          
            }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtenha o nome do item relacionado ao CadastroRespostaItem
        # Isso presume que você está passando um CadastroItem como instância para o formulário
        if self.instance.nome_item:  # Verifique se o CadastroRespostaItem tem um CadastroItem associado
            self.fields['nome_item'].initial = self.instance.nome_item.nome_item  # Defina o valor inicial do campo como o nome do item