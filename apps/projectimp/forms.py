from django import forms
from apps.projectimp.models import IdentificacaoEmpresa, CadastroGrupo

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