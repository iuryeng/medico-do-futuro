from django.contrib import admin
from .models import Paciente, Doenca, Medicamento, Sintoma, Visita, Prescricao

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_nascimento', 'genero', 'email', 'telefone', 'numero_sus']
    search_fields = ['nome', 'email', 'numero_sus']

class SintomaInline(admin.TabularInline):
    model = Sintoma
    extra = 1

class DoencaAdmin(admin.ModelAdmin):
    inlines = [SintomaInline]
    list_display = ['nome']
    search_fields = ['nome']

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'dosagem']
    search_fields = ['nome']

class VisitaAdmin(admin.ModelAdmin):
    list_display = ['data_visita', 'motivo']
    search_fields = ['motivo']

class PrescricaoAdmin(admin.ModelAdmin):
    list_display = ['medicamento', 'dosagem']
    search_fields = ['medicamento__nome']

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Doenca, DoencaAdmin)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Visita, VisitaAdmin)
admin.site.register(Prescricao, PrescricaoAdmin)
