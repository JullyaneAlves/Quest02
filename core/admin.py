from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import *

from django.conf.locale.pt_BR import formats as pt_BR_formats

pt_BR_formats.DATETIME_FORMAT = "d M Y H:i"
pt_BR_formats.DATE_FORMAT = "d M Y"


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'datainicio', 'datatermino', 'horainicio', 'horatermino', 'professor', 'curso')
    date_hierarchy = ('datainicio')
    search_fieldes = ('nome',)
    list_filter = ['datainicio', 'datatermino']

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fone', 'valor')


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Curso, CursoAdmin)
