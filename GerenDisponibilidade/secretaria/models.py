# -*- encoding: utf-8 -*-

from django.db import models

# Create your models here.
class TipoDeSala(models.Model):
    nome = models.CharField('Tipo de Sala', max_length=255)
    descricao = models.TextField('Descrição')

