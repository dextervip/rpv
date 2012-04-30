# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import newDisciplina
from forms import FormNewDisciplina


def lista(request):
    
    lista_disciplinas = newDisciplina.objects.all().order_by("id")
    return render_to_response("disciplina/listaDisc.html", {'lista_disciplinas': lista_disciplinas},
        context_instance=RequestContext(request))


def addDisciplina(request):
    
    if request.method == "POST":
        form = FormNewDisciplina(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("geral/salvo.html", context_instance=RequestContext(request))
    else:
        form = FormNewDisciplina()
    return render_to_response("disciplina/newDisciplina.html", {'form': form},
        context_instance=RequestContext(request))
    

def disciplina(request, nr_disci):
    
    disciplina = get_object_or_404(newDisciplina, pk=nr_disci)
    return render_to_response("disciplina/showDisciplina.html", {'disciplina': disciplina} ,
        context_instance=RequestContext(request))
        
#ainda não esta 100%...
def attInfoDisciplinas(request, nr_disci):
        
    attDiscip = get_object_or_404(newDisciplina, pk=nr_disci)
    if request.method == "POST":
        form = FormNewDisciplina(request.POST, request.FILES, instance=attDiscip)
        if form.is_valid():
            form.save()
            return render_to_response("geral/salvo.html", context_instance=RequestContext(request))
    else:
        form = FormNewDisciplina()
    return render_to_response("disciplina/attInfoDiscip.html", {'attDiscip': attDiscip, 'form': form} ,
        context_instance=RequestContext(request))


def removerDiscip(request):   
    
    # discip = disciplina.objects.get(pk = nr_discp)
    pass


def pesquisaDiscip(request, paramPesq):
    
    #não esta 100%...
    #resultPesq = newDisciplina.objects.filter(nome__istartswitch="paramPesq").order_by("nome")
    #return render_to_response()
    pass