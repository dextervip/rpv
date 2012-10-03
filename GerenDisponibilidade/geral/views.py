# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = RequestContext(request)
    return render_to_response("geral/paginaInicial.html", context)

@login_required
def pageLogin(request):
    context = RequestContext(request)
    return render_to_response("geral/pageHomeLogin.html", context) 
    
@login_required
def sobre(request):
    context = RequestContext(request)
    return render_to_response("geral/sobre.html", context)

@login_required
def contato(request):
    context = RequestContext(request)
    return render_to_response("geral/contato.html", context)