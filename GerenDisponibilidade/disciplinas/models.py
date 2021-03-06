# -*- encoding: utf-8 -*-

from django.db import models

#from professor.models import Curso, Campus

class Disciplina(models.Model):
    
    nome = models.CharField('Componente Curricular', max_length=255)
    #codigo = models.CharField('Código', max_length=50, unique=True)
    codigo = models.CharField('Código', max_length=50)
    #Sera uma listagem com os Cursos ja cadastrados, uma especie de checkBos para selecionar
    curso = models.ManyToManyField('professor.Curso', blank=True, null=True)
    campus = models.ForeignKey('professor.Campus', blank=True, null=True)
    cargaHora = models.CharField('Carga Horária', max_length=5)
    creditosPraticos = models.CharField('Créditos Práticos', max_length=20)
    creditosTeoricos = models.CharField('Créditos Teóricos', max_length=20)
    anoLetivo = models.CharField('Ano Letivo', max_length=10, blank=True)
    turno = models.CharField(max_length=20, blank=True)
    turma = models.CharField(max_length=20, blank=True)
    
    ementa = models.TextField()
    objetivoGeral = models.TextField('Objetivo Geral')
    objetivoEspecif = models.TextField('Objetivo Específico', blank=True)
    #Sera um relacionamento - Combo para escolher as disciplinas já cadastradas... listando as já escolhidas
    preRequisitos = models.TextField('Pré-requisito(s)', blank=True)
    bibliograBasica = models.TextField('Referências Básicas (Leituras Obrigatórias)')
    bibliograComplem = models.TextField('Referências Complementares', blank=True)
    
    def getDisciplinas(self):
        return Disciplina.objects.all()
    
"""
   
    nome = models.CharField(max_length = 255)
    codigo = models.CharField(max_length=50)
    

TERMINAR ESTA REMODELAÇÃO NO MODEL E FORM DE DISCIPLINAS!


    Não esqueça que dados como Professor, 
    Coteudo Programático(de tal a tal semana, sera passada tal matéria - não confundir com cronograma)
    cronograma, metodEnsino, Avaliação do Processo de Ensino e Aprendizagem, 
    Atividades de Recuperação Preventiva do Processo de Ensino e Aprendizagem,
    seram construidos na geração do plano de ensino(Outro grande problema para resolvermos...).
"""
