# -*- encoding: utf-8 -*-

from django.db import models


class newDisciplina(models.Model):
    
    nome = models.CharField(max_length = 150, unique = True)
    codigo = models.CharField(max_length = 50, unique = True)
    #Sera uma listagem com os Cursos ja cadastrados, uma especie de checkBos para selecionar
    curso = models.CharField(max_length = 150, blank=True)
    campus = models.CharField(max_length = 150, blank=True)
    cargaHora = models.CharField(max_length = 5)
    creditosPraticos = models.CharField(max_length = 20, blank=True)
    creditosTeoricos = models.CharField(max_length = 20, blank=True)
    anoLetivo = models.CharField(max_length = 10, blank=True)
    turno = models.CharField(max_length = 20, blank=True)
    turma = models.CharField(max_length = 20, blank=True)
    
    ementa = models.TextField()
    ojetivos = models.TextField()
    #Sera um relacionamento - Combo para escolher as disciplinas já cadastradas... listando as já escolhidas
    preRequisitos = models.TextField(blank=True)
    bibliograBasica = models.TextField()
    bibliograComplem = models.TextField(blank=True)
    
    """ Não esqueça que dados como Professor, 
    Coteudo Programático(de tal a tal semana, sera passada tal matéria - não confundir com cronograma)
    cronograma, metodEnsino, Avaliação do Processo de Ensino e Aprendizagem, 
    Atividades de Recuperação Preventiva do Processo de Ensino e Aprendizagem,
    seram construidos na geração do plano de ensino(Outro grande problema para resolvermos...)."""
