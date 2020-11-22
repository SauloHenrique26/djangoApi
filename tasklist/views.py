from django.shortcuts import render
from rest_framework import viewsets
from tasklist.models import Tarefas,Video
from tasklist.serializer import TarefasSerializer,VideoSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    queryset= Tarefas.objects.all()
    serializer_class= TarefasSerializer

class VideoViewSet (viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class=VideoSerializer

