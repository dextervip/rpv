# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from django.http import HttpResponse
from forms import CadastroCompromisso
from professor.models import Compromisso


def home(request):
    context_instance = RequestContext(request)
    return render_to_response("professor/home.html", context_instance)

def adicionarCompromisso(request):
    if request.method == 'POST':
        form = CadastroCompromisso(request.POST) # A form bound to the POST data
        if form.is_valid():
            return None
        else:
            context_instance = RequestContext(request,{ 'form' : form})
            return render_to_response("professor/adicionar-compromisso.html", context_instance)
    else:
        context_instance = RequestContext(request,{ 'form' : CadastroCompromisso})
        return render_to_response("professor/adicionar-compromisso.html", context_instance)

def getCompromissos(request):
    #colours = ['red', 'blue', 'yellow']
    compromissos = Compromisso.objects.all()
    data = simplejson.dumps(compromissos)
    return HttpResponse(data, mimetype='application/json')
