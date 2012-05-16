# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.
class TipoDeSala(models.Model):
    nome = models.CharField('Tipo de Sala', max_length=255)
    descricao = models.TextField('Descrição')
    
    def __unicode__(self):
        return self.nome


class Sala(models.Model):
    tipo = models.ForeignKey(TipoDeSala, verbose_name='tipo de sala')
    numero = models.CharField('Número', max_length=255)
    capacidade = models.CharField('Capacidade', max_length=255)
    ar_condicionado = models.BooleanField('Ar Condicionado')
    numLugares = models.IntegerField('Número de Lugares')
