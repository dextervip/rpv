# -*- encoding: utf-8 -*-

from django.db import models


class Compromisso(models.Model):
    
        titulo = models.CharField(max_length=80)
        descricao = models.TextField()
        dataInicio = models.DateTimeField()
        dataFim = models.DateTimeField()
        horaInicio = models.TimeField()
        horaFim = models.TimeField()
        
    

