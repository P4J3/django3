from django.contrib import admin
from .models import Servico, Cargo, Funcionario, Feature

# Register your models here.

@admin.register(Servico)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('servico', 'descricao', 'ativo', 'modificado', 'icone')



@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo','ativo','modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'bio')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('nome', 'icone')