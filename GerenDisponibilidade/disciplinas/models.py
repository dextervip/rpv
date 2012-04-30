# -*- encoding: utf-8 -*-

from django.db import models


class newDisciplina(models.Model):
    
    nome = models.CharField(max_length = 150, unique = True)
    ementa = models.TextField()
    #Sera uma listagem com os Cursos ja cadastrados, uma especie de checkBos para selecionar
    curso = models.CharField(max_length = 150)
    codigo = models.CharField(max_length = 50, unique = True)
    cargaHora = models.CharField(max_length = 5)
    creditosPraticos = models.CharField(max_length = 20, blank=True)
    creditosTeoricos = models.CharField(max_length = 20, blank=True)
    #Sera um relacionamento
    professorResp = models.CharField(max_length = 150)
    campus = models.CharField(max_length = 150)
    #Sera um relacionamento
    preRequisitos = models.TextField()
    anoLetivo = models.CharField(max_length = 10)
    turno = models.CharField(max_length = 20)
    turma = models.CharField(max_length = 20)