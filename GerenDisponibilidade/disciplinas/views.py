# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import newDisciplina
from forms import FormNewDisciplina, FormDadosDisci


def lista(request):
    
    lista_disciplinas = newDisciplina.objects.all()
    return render_to_response("disciplina/listaDisc.html", {'lista_disciplinas': lista_disciplinas},
        context_instance=RequestContext(request))


def addDisciplina(request):
    
    if request.method == "POST":
        form = FormNewDisciplina(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("areaGeral/salvo.html", {})
    else:
        form = FormNewDisciplina()
    return render_to_response("disciplina/newDisciplina.html", {'form': form},
        context_instance=RequestContext(request))
    

def disciplina(request, nr_disci):
    
    disciplina = get_object_or_404(newDisciplina, pk=nr_disci)
    if request.method == "POST":
        form = FormDadosDisci(request.POST, request.FILES, instance=disciplina)
        if form.is_valid():
            form.save()
            return render_to_response("areaGeral/salvo.html", {})
    else:
        form = FormDadosDisci()
    return render_to_response("disciplina/disciplina.html", {'disciplina': disciplina, 'form': form} ,
        context_instance=RequestContext(request))
        

def remover(request):
    pass
