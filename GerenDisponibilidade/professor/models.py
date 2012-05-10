# -*- encoding: utf-8 -*-

from django.db import models


class Compromisso(models.Model):
    
        nome = models.CharField(max_length=80)
        descricao = models.TextField()
        dataInicio = models.DateField()
        dataFim = models.DateField()
        horaInicio = models.DateField()
        horaFim = models.DateField()
        
    

