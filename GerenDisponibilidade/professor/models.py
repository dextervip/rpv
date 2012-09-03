# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib import messages
from datetime import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.shortcuts import render_to_response, get_object_or_404
from django.core.validators import MaxLengthValidator
from datetime import timedelta
from calendar import monthrange
from dateutil import relativedelta


class Compromisso(models.Model):
    
        titulo = models.CharField(max_length=80)
        descricao = models.TextField()
        dataInicio = models.DateField()
        dataFim = models.DateField()
        horaInicio = models.TimeField(null=True, blank=True)
        horaFim = models.TimeField(null=True, blank=True)
        diaInteiro = models.BooleanField(default=True)
        publico = models.BooleanField(default=False)
        frequencia = models.IntegerField()
        dataFimFrequencia = models.DateField(null=True, blank=True)
        diaSemana = models.ManyToManyField('DiaSemana')
        
 
class DiaSemana(models.Model):
    
    DIAS_CHOICES = (
                    ("Seg", "Segunda-Feira"),
                    ("Ter", "Terça-Feira"),
                    ("Qua", "Quarta-Feira"),
                    ("Qui", "Quinta-Feira"),
                    ("Sex", "Sexta-Feira"),
                    ("Sab", "Sábado"),
                    ("Dom", "Domingo"),
                    )
           
    dias = models.CharField(max_length=20, choices=DIAS_CHOICES) 
    
       
class Agenda():
    def inserirCompromisso(self, request):
        messages.add_message(request, messages.INFO, 'O compromisso foi adicionado com sucesso em sua agenda!')
        dataI = datetime.strptime(request.POST['dataInicio'], '%d/%m/%Y').strftime('%Y-%m-%d')
        dataF = datetime.strptime(request.POST['dataFim'], '%d/%m/%Y').strftime('%Y-%m-%d')
        c = Compromisso(titulo=request.POST['titulo'],
                            descricao=request.POST['descricao'],
                            dataInicio=dataI,
                            dataFim=dataF,
                            frequencia=request.POST['frequencia'],
                            dataFimFrequencia=datetime.strptime(request.POST['dataFimFrequencia'], '%d/%m/%Y').strftime('%Y-%m-%d')
                        
                            
                            )
        #print request.POST['diaSemana']
        if 'publico' in request.POST:
            c.publico = True
        else:
            c.publico = False
        if request.POST['horaInicio'] == '' :
            c.diaInteiro = True
            c.horaInicio = '00:00:00' 
            c.horaFim = '00:00:00'           
        else:
            c.diaInteiro = False
            c.horaInicio = request.POST['horaInicio']
            c.horaFim = request.POST['horaFim']
        c.save()
        return HttpResponseRedirect(reverse('professor:home'))
            
    def editarCompromisso(self, request, id):
        compromisso = get_object_or_404(Compromisso, pk=id)
        dataI = datetime.strptime(request.POST['dataInicio'], '%d/%m/%Y').strftime('%Y-%m-%d')
        dataF = datetime.strptime(request.POST['dataFim'], '%d/%m/%Y').strftime('%Y-%m-%d')
        compromisso.titulo = request.POST['titulo']
        compromisso.descricao = request.POST['descricao']
        compromisso.dataInicio = dataI
        compromisso.dataFim = dataF
        compromisso.frequencia = request.POST['frequencia']
        compromisso.dataFimFrequencia = datetime.strptime(request.POST['dataFimFrequencia'], '%d/%m/%Y').strftime('%Y-%m-%d')
        
        if 'publico' in request.POST:
            compromisso.publico = True
        else:
            compromisso.publico = False
        if request.POST['horaInicio'] == '' :
            compromisso.diaInteiro = True
            compromisso.horaInicio = '00:00:00' 
            compromisso.horaFim = '00:00:00'           
        else:
            compromisso.diaInteiro = False
            compromisso.horaInicio = request.POST['horaInicio']
            compromisso.horaFim = request.POST['horaFim']
        compromisso.save()
        messages.add_message(request, messages.INFO, 'O compromisso foi editado com sucesso em sua agenda!')
        return HttpResponseRedirect(reverse('professor:home'))
    
    def getCompromisso(self):
        compromissos = Compromisso.objects.all()
        vetor = []
        dateFormat = "%Y-%m-%d"
        for compromisso in compromissos:  
                                                          
            vetor.append({'id' : compromisso.id ,
                          'title' : compromisso.titulo,
                          'start' : datetime.strftime(compromisso.dataInicio , dateFormat) + " " + str(compromisso.horaInicio),
                          'end': datetime.strftime(compromisso.dataFim, dateFormat) + " " + str(compromisso.horaFim),
                          'allDay' : compromisso.diaInteiro,
                          'url' : '/professor/visualizar-compromisso/' + str(compromisso.id),
                          })
            
            #verifica repeticao todos os dias
            if(compromisso.frequencia == 1):  
                delta = compromisso.dataFimFrequencia - compromisso.dataInicio
                for i in range(1, (delta.days + 1)):
                    vetor.append({'id' : compromisso.id ,
                          'title' : compromisso.titulo,
                          'start' : datetime.strftime((compromisso.dataInicio + timedelta(days=i)), dateFormat) + " " + str(compromisso.horaInicio),
                          'end': datetime.strftime((compromisso.dataFim + timedelta(days=i)), dateFormat) + " " + str(compromisso.horaFim),
                          'allDay' : compromisso.diaInteiro,
                          'url' : '/professor/visualizar-compromisso/' + str(compromisso.id),
                          })
                    
            #verifica repeticao todos os meses
            if(compromisso.frequencia == 3):  
                delta = relativedelta.relativedelta(compromisso.dataFimFrequencia, compromisso.dataInicio)
                #return HttpResponse(delta.months)
                for i in range(1, delta.months):
                    vetor.append({'id' : compromisso.id ,
                          'title' : compromisso.titulo,
                          'start' : datetime.strftime((compromisso.dataInicio + relativedelta.relativedelta(months= +i)), dateFormat) + " " + str(compromisso.horaInicio),
                          'end': datetime.strftime((compromisso.dataFim + relativedelta.relativedelta(months= +i)), dateFormat) + " " + str(compromisso.horaFim),
                          'allDay' : compromisso.diaInteiro,
                          'url' : '/professor/visualizar-compromisso/' + str(compromisso.id),
                          })
                    
            #verifica repeticao todos os semestres
            #if(compromisso.frequencia == 3):  
            #    delta = relativedelta.relativedelta(compromisso.dataFimFrequencia, compromisso.dataInicio)
                #return HttpResponse(delta.months)
            #    for i in range(1, delta.months):
            #        vetor.append({'id' : compromisso.id ,
            #              'title' : compromisso.titulo,
            #              'start' : datetime.strftime((compromisso.dataInicio + relativedelta.relativedelta(months= +i)), dateFormat) + " " + str(compromisso.horaInicio),
            #              'end': datetime.strftime((compromisso.dataFim + relativedelta.relativedelta(months= +i)), dateFormat) + " " + str(compromisso.horaFim),
            #              'allDay' : compromisso.diaInteiro,
            #              'url' : '/professor/visualizar-compromisso/' + str(compromisso.id),
            #              })
                    
            #verifica repeticao todos os anos
            if(compromisso.frequencia == 5):  
                delta = relativedelta.relativedelta(compromisso.dataFimFrequencia, compromisso.dataInicio)
                #return HttpResponse(delta.years)
                for i in range(1, delta.years):
                    vetor.append({'id' : compromisso.id ,
                          'title' : compromisso.titulo,
                          'start' : datetime.strftime((compromisso.dataInicio + relativedelta.relativedelta(years= +i)), dateFormat) + " " + str(compromisso.horaInicio),
                          'end': datetime.strftime((compromisso.dataFim + relativedelta.relativedelta(years= +i)), dateFormat) + " " + str(compromisso.horaFim),
                          'allDay' : compromisso.diaInteiro,
                          'url' : '/professor/visualizar-compromisso/' + str(compromisso.id),
                          })
      
        data = simplejson.dumps(vetor);
        return HttpResponse(data, mimetype='application/json')
    
    def excluirCompromisso(self, request, id):
        compromisso = get_object_or_404(Compromisso, pk=id)
        compromisso.delete()
        messages.add_message(request, messages.INFO, 'O compromisso foi excluido com sucesso da sua agenda!')
        return HttpResponseRedirect(reverse('professor:home'))
    
    
