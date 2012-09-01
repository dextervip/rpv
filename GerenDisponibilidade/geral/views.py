# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    context = RequestContext(request)
    return render_to_response("geral/paginaInicial.html", context)


def sobre(request):
    context = RequestContext(request)
    return render_to_response("geral/sobre.html", context)

def contato(request):
    context = RequestContext(request)
    return render_to_response("geral/contato.html", context)