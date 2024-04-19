from django.db import models

class IdentificacaoEmpresa(models.Model):
    nome_empresa = models.CharField(max_length=200, null=False, blank=False) 
    email_empresa = models.EmailField(max_length=200, null=False, blank=False)
    fone_empresa = models.CharField(max_length=200, null=False, blank=False)
    cnpj_empresa = models.CharField(max_length=200, null=False, blank=False)
        
    def __str__(self):
       return self.nome_empresa

class CadastroGrupo(models.Model):
    nome_grupo = models.CharField(max_length=200, null=False, blank=False) 
    ordem_grupo = models.IntegerField(null=False, blank=False)
    ativo = models.BooleanField(default=False)

    def __str__(self):
       return self.nome_grupo

class CadastroSubGrupo(models.Model):
    nome_subgrupo = models.CharField(max_length=200, null=False, blank=False) 
    ordem_subgrupo = models.IntegerField(null=False, blank=False)
    ativo = models.BooleanField(default=False)
    nome_grupo = models.ForeignKey(
        to=CadastroGrupo,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="grupo"
    )

    def __str__(self):
       return self.nome_subgrupo
    
class CadastroItem(models.Model):
    TIPO_CHOICES = [
        ('list', 'Lista'),
        ('checkbox', 'Caixa de Seleção'),
        ('descritivo', 'Descritivo'),
    ]
     
    nome_item = models.CharField(max_length=200, null=False, blank=False) 
    ordem_item = models.IntegerField(null=False, blank=False)
    ativo = models.BooleanField(default=False)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    contador = models.IntegerField(null=False, blank=False)
    Opcional = models.BooleanField(default=False)
    Unidade =models.IntegerField(null=False, blank=False)
    nome_subgrupo = models.ForeignKey(
        to=CadastroSubGrupo,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="subgrupo"
    )
    lista = models.ForeignKey('Lista', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
       return self.nome_item
    
class CadastroRespostaItem(models.Model):
    resposta_item = models.CharField(max_length=200, null=False, blank=False)
    nome_item = models.ForeignKey(
        to=CadastroItem,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="item"
    )

    def __str__(self):
       return self.resposta_item
    
class Lista(models.Model):
    nome = models.CharField(max_length=100)
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class OpcaoLista(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.descricao