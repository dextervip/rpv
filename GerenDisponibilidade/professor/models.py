# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib import messages
from datetime import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.shortcuts import render_to_response, get_object_or_404


class Compromisso(models.Model):
    
        titulo = models.CharField(max_length=80)
        descricao = models.TextField()
        dataInicio = models.DateField()
        dataFim = models.DateField()
        horaInicio = models.TimeField(null=True, blank=True)
        horaFim = models.TimeField(null=True, blank=True)
        diaInteiro = models.BooleanField(default=True)
        publico = models.BooleanField(default=False)
        
class Agenda():
    def inserirCompromisso(self, request):
        messages.add_message(request, messages.INFO, 'O compromisso foi adicionado com sucesso em sua agenda!')
        dataI = datetime.strptime(request.POST['dataInicio'], '%d/%m/%Y').strftime('%Y-%m-%d')
        dataF = datetime.strptime(request.POST['dataFim'], '%d/%m/%Y').strftime('%Y-%m-%d')
        c = Compromisso(titulo=request.POST['titulo'],
                            descricao=request.POST['descricao'],
                            dataInicio=dataI,
                            dataFim=dataF,
                            
                            )
        if 'publico' in request.POST:
            c.publico = True
        else:
            c.publico = False
        if request.POST['horaInicio'] == '' :
            c.diaInteiro = True           
        else:
            c.diaInteiro = False
            c.horaInicio = request.POST['horaInicio']
            c.horaFim = request.POST['horaFim']            
        c.save()
        return HttpResponseRedirect(reverse('professor:home'))
    
    def getCompromisso(self):
        compromissos = Compromisso.objects.all()
        vetor = []
        dateFormat = "%Y, %m, %d"
        for compromisso in compromissos:            
            vetor.append({'id' : compromisso.id ,
                          'title' : compromisso.titulo,
                          'start' : datetime.strftime(compromisso.dataInicio , dateFormat) ,
                          'end': datetime.strftime(compromisso.dataFim, dateFormat),
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
    

