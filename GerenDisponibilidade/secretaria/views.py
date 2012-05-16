# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import TipoDeSala
from models import Sala
from forms import FormTipoDeSala
from forms import FormSala

def listaTipos(request):
    
    lista_tipos_sala = TipoDeSala.objects.all().order_by("id")
    return render_to_response("secretaria/listaTipos.html", {'lista_tipos_sala': lista_tipos_sala},
        context_instance=RequestContext(request))

def listaSalas(request):
    
    lista_salas = Sala.objects.all().order_by("id")
    return render_to_response("secretaria/listaSalas.html", {'lista_salas': lista_salas},
        context_instance=RequestContext(request))


def addTipoDeSala(request):
        
    if request.method == "POST":
        form = FormTipoDeSala(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("geral/salvo.html", context_instance=RequestContext(request))
    else:
        form = FormTipoDeSala()
    return render_to_response("secretaria/novoTipoSala.html", {'form': form},
        context_instance=RequestContext(request))
    

def addSala(request):
        
    if request.method == "POST":
        form = FormSala(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("geral/salvo.html", context_instance=RequestContext(request))
    else:
        form = FormSala()
    return render_to_response("secretaria/novaSala.html", {'form': form},
        context_instance=RequestContext(request))


def tipoDeSala(request, nr_tipo):
    
    tipo_sala = get_object_or_404(TipoDeSala, pk=nr_tipo)
    return render_to_response("secretaria/showTipoDeSala.html", {'tipo': tipo_sala} ,
        context_instance=RequestContext(request))


def s_sala(request, nr_sala):
    
    sala = get_object_or_404(Sala, pk=nr_sala)
    return render_to_response("secretaria/showSala.html", {'sala': sala} ,
        context_instance=RequestContext(request))


def editarTipoSala(request, nr_tipo):
        
    editTipo = get_object_or_404(TipoDeSala, pk=nr_tipo)
    if request.method == "POST":
        form = FormTipoDeSala(request.POST, instance=editTipo)
        if form.is_valid():
            form.save()
            return render_to_response("geral/salvo.html", context_instance=RequestContext(request))
    else:
        form = FormTipoDeSala(instance=editTipo)
    return render_to_response("secretaria/editarTipoSala.html", {'editTipo': editTipo, 'form': form} ,
        context_instance=RequestContext(request))



def editarSala(request, nr_sala):
        
    editSala = get_object_or_404(Sala, pk=nr_sala)
    if request.method == "POST":
        form = FormSala(request.POST, instance=editSala)
        if form.is_valid():
            form.save()
            return render_to_response("geral/salvo.html", context_instance=RequestContext(request))
    else:
        form = FormSala(instance=editSala)
    return render_to_response("secretaria/editarSala.html", {'editSala': editSala, 'form': form} ,
        context_instance=RequestContext(request))


def removerTipoSala(request, nr_tipo):   
    
    removeTipo = get_object_or_404(TipoDeSala, pk=nr_tipo)
    if request.method == "POST":
        removeTipo.delete()
        return render_to_response("geral/dadosRemovidos.html", context_instance=RequestContext(request))
    else:
        return render_to_response("secretaria/remover.html", {'removeTipoSala': removeTipo} ,
        context_instance=RequestContext(request))

def removerSala(request, nr_sala):   
    
    removeSala = get_object_or_404(Sala, pk=nr_sala)
    if request.method == "POST":
        removeSala.delete()
        return render_to_response("geral/dadosRemovidos.html", context_instance=RequestContext(request))
    else:
        return render_to_response("secretaria/removerSala.html", {'removeSala': removeSala} ,
        context_instance=RequestContext(request))


def pesquisaTipoSala(request):
    
    if request.method == "POST":
        paramPesq = request.POST.get('pesquisa')
        resultPesq = TipoDeSala.objects.filter(nome__icontains=paramPesq).order_by("nome")
        return render_to_response("secretaria/pesquisaTipos.html", {'resultPesq': resultPesq},
                              context_instance=RequestContext(request))

def pesquisaSala(request):
    
    if request.method == "POST":
        paramPesq = request.POST.get('pesquisa')
        resultPesq = Sala.objects.filter(numero__icontains=paramPesq).order_by("numero")
        return render_to_response("secretaria/pesquisaSalas.html", {'resultPesq': resultPesq},
                              context_instance=RequestContext(request))
