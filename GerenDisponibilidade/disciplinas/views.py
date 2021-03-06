# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import Disciplina
from forms import FormNewDisciplina
from django.contrib.auth.decorators import login_required

@login_required
def lista(request):
    
    lista_disciplinas = Disciplina.objects.all().order_by("id")
    return render_to_response("disciplina/listaDisc.html", {'lista_disciplinas': lista_disciplinas},
        context_instance=RequestContext(request))

@login_required
def addDisciplina(request):
        
    if request.method == "POST":
        form = FormNewDisciplina(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("geral/salvo.html", context_instance=RequestContext(request))
    else:
        form = FormNewDisciplina()
    return render_to_response("disciplina/Disciplina.html", {'form': form},
        context_instance=RequestContext(request))
    
@login_required
def disciplina(request, nr_disci):
    
    disciplina = get_object_or_404(Disciplina, pk=nr_disci)
    return render_to_response("disciplina/showDisciplina.html", {'disciplina': disciplina} ,
        context_instance=RequestContext(request))
        
@login_required
def editarDiscip(request, nr_disci):
        
    editDiscip = get_object_or_404(Disciplina, pk=nr_disci)
    if request.method == "POST":
        form = FormNewDisciplina(request.POST, instance=editDiscip)
        if form.is_valid():
            form.save()
            return render_to_response("geral/salvo.html", context_instance=RequestContext(request))
    else:
        form = FormNewDisciplina(instance=editDiscip)
    return render_to_response("disciplina/editarDiscip.html", {'editDiscip': editDiscip, 'form': form} ,
        context_instance=RequestContext(request))

@login_required
def removerDiscip(request, nr_discp):   
    
    removeDiscip = get_object_or_404(Disciplina, pk=nr_discp)
    if request.method == "POST":
        removeDiscip.delete()
        return render_to_response("geral/dadosRemovidos.html", context_instance=RequestContext(request))
    else:
        return render_to_response("geral/remover.html", {'removeDiscip': removeDiscip} ,
        context_instance=RequestContext(request))
        
@login_required
def pesquisaDiscip(request):
    
    if request.method == "POST":
        paramPesq = request.POST.get('pesquisa')
        resultPesq = Disciplina.objects.filter(nome__icontains=paramPesq).order_by("nome")
        return render_to_response("disciplina/pesquisaDiscip.html", {'resultPesq': resultPesq},
                              context_instance=RequestContext(request))
    else:
        return render_to_response("disciplina/pesquisaDiscip.html", context_instance=RequestContext(request))
