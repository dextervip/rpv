# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from forms import CadastroCompromisso
from professor.models import Compromisso
from datetime import datetime
from django.core.urlresolvers import reverse

def home(request):
    context_instance = RequestContext(request)
    return render_to_response("professor/home.html", context_instance)

def adicionarCompromisso(request):
    if request.method == 'POST':
        form = CadastroCompromisso(request.POST) # A form bound to the POST data
        if form.is_valid():
            dataI = datetime.strptime(request.POST['dataInicio'], '%d/%m/%Y').strftime('%Y-%m-%d')
            dataF = datetime.strptime(request.POST['dataFim'], '%d/%m/%Y').strftime('%Y-%m-%d')
            c = Compromisso(titulo=request.POST['titulo'],
                            descricao=request.POST['descricao'],
                            dataInicio=dataI,
                            dataFim=dataF,
                            horaInicio=request.POST['horaInicio'],
                            horaFim=request.POST['horaFim'])
            c.save()
            return HttpResponseRedirect(reverse('professor:home'))
        else:
            context_instance = RequestContext(request, { 'form' : form})
            return render_to_response("professor/adicionar-compromisso.html", context_instance)
    else:
        context_instance = RequestContext(request, { 'form' : CadastroCompromisso})
        return render_to_response("professor/adicionar-compromisso.html", context_instance)

def getCompromissos(request):
    compromissos = Compromisso.objects.all()
    vetor = []
    dateFormat = "%Y, %m, %d"
    for compromisso in compromissos:
        vetor.append({'title' : compromisso.titulo, 'start' : datetime.strftime(compromisso.dataInicio, dateFormat) , 'end': datetime.strftime(compromisso.dataFim, dateFormat)})
    data = simplejson.dumps(vetor);
    return HttpResponse(data, mimetype='application/json')
