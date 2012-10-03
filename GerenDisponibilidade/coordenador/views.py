# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = RequestContext(request)
    return render_to_response("coordenador/home.html", context)

@login_required
def montarGradeAula(request):
    context = RequestContext(request)
    return render_to_response("coordenador/montarGradeAula.html", context)

