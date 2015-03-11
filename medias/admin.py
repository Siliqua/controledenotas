from django.contrib import admin
from medias.models import Disciplina


class AgendaAdmin(admin.ModelAdmin):
    admin.site.register(Disciplina)