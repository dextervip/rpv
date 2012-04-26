# -*- encoding: utf-8 -*-

from django.db import models


class newDisciplina(models.Model):
    
    titulo = models.CharField(max_length = 150)
    ementa = models.TextField()
    
    
class compleDisci(models.Model):
    
    cargaHora = models.CharField(max_length = 5)
    creditosPraticos = models.CharField(max_length = 5)
    creditosTeoricos = models.CharField(max_length = 5)
    #Sera um relacionamento
    professorResp = models.CharField(max_length = 150)
    campus = models.CharField(max_length = 100)
    #Sera uma listagem com os Cursos ja cadastrados, uma especie de checkBos para selecionar
    curso = models.CharField(max_length = 100)
    #Sera um relacionamento
    preRequisitos = models.TextField()
    anoLetivo = models.CharField(max_length = 20)
    turno = models.CharField(max_length = 20)
    turma = models.CharField(max_length = 20)
    
