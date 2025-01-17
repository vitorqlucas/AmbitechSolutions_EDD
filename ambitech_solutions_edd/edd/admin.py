#from django.contrib import admin
#from .models import *
#from django.contrib.auth.admin import UserAdmin
## Register your models here.
#
#campos = list(UserAdmin.fieldsets)
#campos.append(("Informações adicionais", {'fields': ('cnpj_cpf', 'data_compra', 'ativo')}))
#
#UserAdmin.fieldsets = tuple(campos)
#
#admin.site.register(Cliente, UserAdmin)
from django.contrib import admin
from .models import Cliente
from django.contrib.auth.admin import UserAdmin

# Personalizando o UserAdmin para incluir os campos adicionais
class ClienteAdmin(UserAdmin):
    # Adicionando os campos extras ao fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ("Informações adicionais", {'fields': ('cnpj_cpf', 'data_compra', 'ativo')}),
    )

    # Configurando os campos para o formulário de criação (opcional)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Informações adicionais", {'fields': ('cnpj_cpf', 'data_compra', 'ativo')}),
    )

    # Campos que serão exibidos na listagem de usuários
    list_display = ('username', 'email', 'cnpj_cpf', 'data_compra', 'ativo', 'is_staff')
    list_filter = ('ativo', 'is_staff', 'is_superuser', 'data_compra', 'groups')

# Registrando o modelo personalizado
admin.site.register(Cliente, ClienteAdmin)
