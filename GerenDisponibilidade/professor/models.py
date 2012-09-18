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
from disciplinas.models import Disciplina


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
           
    nome = models.CharField(max_length=20, choices=DIAS_CHOICES) 
    nome_curto = models.CharField(max_length=20, choices=DIAS_CHOICES)
    
    def diasSemana(self):
        return [('seg','Segunda'),('ter','Terça'),('qua','Quarta'),('qui','Quinta'),('sex','Sexta'),('sab','Sabado'),('dom','Domingo')]
    
       
class Agenda():
    def inserirCompromisso(self, request):
        messages.add_message(request, messages.INFO, 'O compromisso foi adicionado com sucesso em sua agenda!')
        dataI = datetime.strptime(request.POST['dataInicio'], '%d/%m/%Y').strftime('%Y-%m-%d')
        dataF = datetime.strptime(request.POST['dataFim'], '%d/%m/%Y').strftime('%Y-%m-%d')
        compromisso = Compromisso(titulo=request.POST['titulo'],
                            descricao=request.POST['descricao'],
                            dataInicio=dataI,
                            dataFim=dataF,
                            frequencia=request.POST['frequencia'],
                            dataFimFrequencia=datetime.strptime(request.POST['dataFimFrequencia'], '%d/%m/%Y').strftime('%Y-%m-%d')
                        
                            
                            )
        diaSemanas = request.POST.getlist('diaSemana')
        for diaSemana in diaSemanas:
            d, created = DiaSemana.objects.get_or_create(dias=diaSemana)
            if created == True:
                d.nome_curto = diaSemana;
                d.save() 
            compromisso.save()
            compromisso.diaSemana.add(d);
           
    
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
        
        compromisso.diaSemana.clear()
        diaSemanas = request.POST.getlist('diaSemana')
        for diaSemana in diaSemanas:
            d, created = DiaSemana.objects.get_or_create(dias=diaSemana)
            if created == True:
                d.nome_curto = diaSemana;
                d.save() 
            compromisso.save()
            compromisso.diaSemana.add(d);
        
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
                #delta = relativedelta.relativedelta(compromisso.dataInicio,compromisso.dataFimFrequencia )
                delta = self.monthdelta(compromisso.dataInicio, compromisso.dataFimFrequencia)
                #return HttpResponse(self.monthdelta(compromisso.dataInicio, compromisso.dataFimFrequencia))
                for i in range(1, delta):
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
                return HttpResponse(delta.years)
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

    def monthdelta(self, d1, d2):
        delta = 0
        while True:
            mdays = monthrange(d1.year, d1.month)[1]
            d1 += timedelta(days=mdays)
            if d1 <= d2:
                delta += 1
            else:
                break
        return delta
    
class DisponibilidadeAula(models.Model):
    hora = models.TimeField()
    diaSemana = models.ForeignKey(DiaSemana, blank=True, null=True)
    
    def diasSemana(self):
        return [('seg','Segunda'),('ter','Terça'),('qua','Quarta'),('qui','Quinta'),('sex','Sexta'),('sab','Sabado'),('dom','Domingo')]
    
    def horas(self):
        vetor = []
        hora = datetime(1,1,1,6,30)
        for i in range(1, 16):
            hora = hora + timedelta(hours=1)
            vetor.append(hora.time())
        return vetor
    
    
                
     
class Professor(models.Model):
    nome = models.CharField(max_length=30)
    disponibilidadeAula = models.ManyToManyField('DisponibilidadeAula')
    areaFormacao = models.ManyToManyField('AreaFormacao')
    nivelInteresse = models.ManyToManyField('NivelInteresse')
    
    def getDisponibilidadeAulas(self):
        return self.disponibilidadeAula.select_related().all()
    
    def getDisponibilidadeAula(self, dia, hora):
        d = DiaSemana.objects.get(nome_curto=dia)
        try:
            dis = self.disponibilidadeAula.select_related().get(diaSemana=d, hora=hora)
        except Exception:
            return False
        return dis
    
    def adicionarDisponibilidadeAula(self, dis):
        self.disponibilidadeAula.add(dis)
        
    def removeDisponibilidadeAula(self, dis):
        self.disponibilidadeAula.remove(dis)
        
    def informarDisponibilidade(self, dia, hora):
        ds = DiaSemana.objects.get(nome_curto=dia);
        dis, created = DisponibilidadeAula.objects.get_or_create(diaSemana=ds, hora=hora)
        if created == True:
            dis.hora = hora
            dis.save()
            dis.diaSemana=ds
            dis.save()
        
        if isinstance(self.getDisponibilidadeAula(dia, hora), DisponibilidadeAula):
            self.removeDisponibilidadeAula(dis)
            result = 'removed'
        else:
            self.adicionarDisponibilidadeAula(dis)
            result = 'added'
        
        self.save()
        return {'result' : result , 'dia' : dia,'hora': hora}
    
class AreaFormacao(models.Model):
    nome = models.CharField(max_length=30)
    
class Curso(models.Model):
    nome = models.CharField(max_length=30)
    def __unicode__(self):
        return self.nome
    class Meta:
        ordering = ['nome']
    
class Campus(models.Model):
    nome = models.CharField(max_length=30)
    def __unicode__(self):
        return self.nome
    
class NivelInteresse(models.Model):
    disciplina = models.ForeignKey(Disciplina)
    nivel = models.IntegerField()
    
    
