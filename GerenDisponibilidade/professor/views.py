# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from forms import CadastroCompromisso
from professor.models import Compromisso,Agenda
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib import messages

def home(request):
    context_instance = RequestContext(request)
    return render_to_response("professor/home.html", context_instance)

def adicionarCompromisso(request):
    form = CadastroCompromisso()
    if request.method == 'POST':
        form = CadastroCompromisso(request.POST) 
        if form.is_valid():
            agenda = Agenda()
            return agenda.inserirCompromisso(request)
    context_instance = RequestContext(request, { 'form' : form})
    return render_to_response("professor/adicionar-compromisso.html", context_instance)

def editarCompromisso(request):
    return None
def visualizarCompromisso(request):
    return None
def excluirCompromisso(request):
    return None
def getCompromissos(request):
    agenda = Agenda()
    return agenda.getCompromisso()
