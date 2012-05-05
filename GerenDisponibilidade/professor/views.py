# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


def home(request):
    context_instance = RequestContext(request)
    return render_to_response("professor/home.html", context_instance)