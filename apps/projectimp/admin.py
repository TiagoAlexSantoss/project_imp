from django.contrib import admin
from apps.projectimp.models import CadastroGrupo, CadastroSubGrupo, CadastroItem, IdentificacaoEmpresa, Lista, OpcaoLista

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
    list_display_links = ("id", "nome_item", "nome_subgrupo")
    search_fields = ("nome_item", "nome_subgrupo")
    list_filter = ("nome_subgrupo", "ativo")
    list_editable = ("ativo",)
    list_per_page = 20

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Verifique se o objeto já existe (edição) e se o tipo é 'lista'
        if obj and obj.tipo == 'list':
            # Habilitar o campo lista
            form.base_fields['lista'].disabled = False
        else:
            # Desabilitar o campo lista
            form.base_fields['lista'].disabled = True
        return form

    class Media:
        js = ('js/admin/cadastroitem_admin.js',)

admin.site.register(CadastroItem, ItemAdmin)

class OpcaoListaInline(admin.TabularInline):
    model = OpcaoLista
    extra = 1

class ListaAdmin(admin.ModelAdmin):
    inlines = [OpcaoListaInline]

admin.site.register(Lista, ListaAdmin)
admin.site.register(OpcaoLista)