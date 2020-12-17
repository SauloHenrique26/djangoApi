from django.db import models

class Tarefas(models.Model):
    tarefa = models.CharField(max_length=50)
    observ = models.CharField(max_length=500)
    hora = models.DateTimeField()
    status = models.BooleanField()

    def __str__(self):
        return self.tarefa

class Video(models.Model):
    titulo = models.CharField(max_length=50)
    link = models.CharField(max_length=500)
    
    def __str__(self):
        return self.titulo
