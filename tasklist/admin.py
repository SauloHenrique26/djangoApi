from django.contrib import admin
from tasklist.models import Tarefas,Video

class Tarefa (admin.ModelAdmin):
    list_display = ('id','tarefa','observ','hora','status')
    list_display_links = ('tarefa','observ','hora','status')
    search_fields = ('tarefa','observ','hora','status')

admin.site.register(Tarefas,Tarefa)

class Videos (admin.ModelAdmin):
    list_display = ('id','titulo','link')
    list_display_links = ('titulo','link')
    search_fields = ('titulo','link')

admin.site.register(Video,Videos)