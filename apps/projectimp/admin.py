from django.contrib import admin
from apps.projectimp.models import CadastroGrupo, CadastroSubGrupo, CadastroItem, IdentificacaoEmpresa

class SalvarEmpresa(admin.ModelAdmin):
    list_display = ("id", "nome_empresa", "email_empresa", "fone_empresa")
    list_display_links = ("id", "nome_empresa")
    search_fields = ("nome_empresa",)
    list_filter = ("id", "nome_empresa")
    list_editable = ("nome_empresa",)
    list_per_page = 10


class SalvarGrupoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome_grupo", "ordem_grupo", "ativo")
    list_display_links = ("id", "nome_grupo")
    search_fields = ("nome_grupo",)
    list_filter = ("id", "nome_grupo")
    list_editable = ("ativo",)
    list_per_page = 10

admin.site.register(CadastroGrupo, SalvarGrupoAdmin)

class SalvarSubGrupoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome_subgrupo", "ordem_subgrupo", "nome_grupo","ativo")
    list_display_links = ("id", "nome_subgrupo")
    search_fields = ("nome_subgrupo",)
    list_filter = ("id", "nome_subgrupo")
    list_editable = ("ativo",)
    list_per_page = 10

admin.site.register(CadastroSubGrupo, SalvarSubGrupoAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "nome_item", "ordem_item", "tipo", "nome_subgrupo","ativo")
    list_display_links = ("id", "nome_item")
    search_fields = ("nome_item",)
    list_filter = ("id", "nome_item")
    list_editable = ("ativo",)
    list_per_page = 10

admin.site.register(CadastroItem, ItemAdmin)
