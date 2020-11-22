from rest_framework import serializers
from tasklist.models import Tarefas,Video

class TarefasSerializer (serializers.ModelSerializer):
    class Meta:
        model = Tarefas
        fields = ['id','tarefa','observ','hora','status']


class VideoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id','titulo','link']