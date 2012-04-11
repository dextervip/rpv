# -*- coding: utf-8 -*-
from django.http import HttpResponse

def home(request):
    return HttpResponse('Ola, este é um teste do django...')

