# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import TipoDeSala
from forms import FormTipoDeSala

def listaTipos(request):
    
    lista_tipos_sala = TipoDeSala.objects.all().order_by("id")
    return render_to_response("secretaria/listaTipos.html", {'lista_tipos_sala': lista_tipos_sala},
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


def tipoDeSala(request, nr_tipo):
    
    tipo_sala = get_object_or_404(TipoDeSala, pk=nr_tipo)
    return render_to_response("secretaria/showTiposSala.html", {'tipo': tipo_sala} ,
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


def removerTipoSala(request, nr_tipo):   
    
    removeTipo = get_object_or_404(TipoDeSala, pk=nr_tipo)
    if request.method == "POST":
        removeTipo.delete()
        return render_to_response("geral/dadosRemovidos.html", context_instance=RequestContext(request))
    else:
        return render_to_response("geral/remover.html", {'removeTipoSala': removeTipo} ,
        context_instance=RequestContext(request))


def pesquisaTipoSala(request):
    
    if request.method == "POST":
        paramPesq = request.POST.get('pesquisa')
        resultPesq = TipoDeSala.objects.filter(nome__icontains=paramPesq).order_by("nome")
        return render_to_response("secretaria/pesquisaTipos.html", {'resultPesq': resultPesq},
                              context_instance=RequestContext(request))
