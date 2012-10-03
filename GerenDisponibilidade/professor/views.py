# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from forms import CadastroCompromisso
from professor.models import Compromisso, Agenda, DisponibilidadeAula, Professor, NivelInteresse
from datetime import datetime, time, timedelta
from django.core.urlresolvers import reverse
from django.contrib import messages
from disciplinas.models import Disciplina
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    dis = DisponibilidadeAula()
    disc = Disciplina()
    context_instance = RequestContext(request, {'horas':dis.horas(),'dias': dis.diasSemana(), 'disciplinas' : disc.getDisciplinas() })
    return render_to_response("professor/home.html", context_instance)

@login_required
def adicionarCompromisso(request):
    form = CadastroCompromisso()
    if request.method == 'POST':
        form = CadastroCompromisso(request.POST) 
        if form.is_valid():
            agenda = Agenda()
            return agenda.inserirCompromisso(request)
    context_instance = RequestContext(request, { 'form' : form})
    return render_to_response("professor/adicionar-compromisso.html", context_instance)

@login_required
def editarCompromisso(request, id):
    c = get_object_or_404(Compromisso, pk=id)
    form = CadastroCompromisso(instance=c)
    if request.method == 'POST':
        form = CadastroCompromisso(request.POST) 
        if form.is_valid():
            agenda = Agenda()
            return agenda.editarCompromisso(request, id)
    context_instance = RequestContext(request, { 'form' : form})
    return render_to_response("professor/editar-compromisso.html", context_instance)

@login_required
def visualizarCompromisso(request, id):
    compromisso = get_object_or_404(Compromisso, pk=id)
    context_instance = RequestContext(request, { 'compromisso' : compromisso})
    return render_to_response("professor/visualizar-compromisso.html", context_instance)

@login_required
def excluirCompromisso(request, id):
    agenda = Agenda()
    return agenda.excluirCompromisso(request, id)

@login_required
def getCompromissos(request):
    agenda = Agenda()
    return agenda.getCompromisso() 

@login_required
def disponibilidadeAula(request):
    p = Professor.objects.get(id=1);
    result = p.informarDisponibilidade(request.GET['dia'], request.GET['hora'])
    data = simplejson.dumps(result);
    return HttpResponse(data, mimetype='application/json')

@login_required
def getDisponibilidadeAula(request):
    from django.core import serializers
    p = Professor.objects.get(id=1);
    result = p.getDisponibilidadeAulas()
    vetor = []
    for r in result:
        vetor.append({'hora':  r.hora.strftime("%H:%M") , 'dia':r.diaSemana.nome_curto})
        
    data = simplejson.dumps(vetor);
    return HttpResponse(data, mimetype='application/json')

@login_required
def informarInteresseDisciplina(request):
    professor = Professor.objects.get(id=1);
    discip = Disciplina.objects.get(pk=request.GET['idDisciplina'])
    nivel, created = NivelInteresse.objects.get_or_create(disciplina=discip, nivel=request.GET['nivel'])
    if created == True:
        nivel.nivel = request.GET['nivel']
        nivel.save()
        nivel.disciplina = discip
        nivel.save()

    if professor.nivelInteresse.filter(disciplina=discip).exists() == True:
        n = professor.nivelInteresse.filter(disciplina=discip)[0]
        professor.nivelInteresse.remove(n)
        professor.adicionarNivelInteresse(nivel)
    else:
        professor.adicionarNivelInteresse(nivel)
    professor.save()
    
    return HttpResponse([], mimetype='application/json')

@login_required
def getInteressesDisciplina(request):
    professor = Professor.objects.get(id=1);
    niveis = professor.getNiveisInteresse()
    vetor = []
    for n in niveis:
        vetor.append({'idDisciplina':  n.disciplina.pk , 'nivel': n.nivel})
    data = simplejson.dumps(vetor);
    return HttpResponse(data, mimetype='application/json')
    
    
    