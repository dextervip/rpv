# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from django.http import HttpResponse


def home(request):
    context_instance = RequestContext(request)
    return render_to_response("professor/home.html", context_instance)

def adicionarCompromisso(request):
    context_instance = RequestContext(request)
    return render_to_response("professor/adicionar-compromisso.html", context_instance)

def getCompromisso(request):
    colours = ['red', 'blue', 'yellow']
    data = simplejson.dumps(colours)
    return HttpResponse(data, mimetype='application/json')
