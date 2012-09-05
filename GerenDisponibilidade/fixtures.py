# -*- encoding: utf-8 -*-

from professor.models import Professor, AreaFormacao, DisponibilidadeAula, DiaSemana

class Fixtures(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def load(self):
        print "Loading fixtures into database..."
        #============================
        #Carregando areas de formação
        #============================
        af1 = AreaFormacao()
        af1.nome = "Computação"
        af1.save()
        
        af2 = AreaFormacao()
        af2.nome = "Engenharia Civil"
        af2.save()
        
        af3 = AreaFormacao()
        af3.nome = "Engenharia de Software"
        af3.save()
        
        #============================
        #Carregando professores
        #============================
        p = Professor()
        p.nome = "João Pablo"
        p.save()
        p.areaFormacao.add(af1)
        p.areaFormacao.add(af3)
        p.save()
        
        #=========================
        #Carregando dias da semana
        #=========================
        dis = DiaSemana()
        dis.nome_curto = "seg"
        dis.nome = "Segunda"
        dis.save()
        
        dis1 = DiaSemana()
        dis1.nome_curto = "ter"
        dis1.nome = "Terça"
        dis1.save()
        
        dis2 = DiaSemana()
        dis2.nome_curto = "qua"
        dis2.nome = "Quarta"
        dis2.save()
        
        dis3 = DiaSemana()
        dis3.nome_curto = "qui"
        dis3.nome = "Quinta"
        dis3.save()
        
        dis4 = DiaSemana()
        dis4.nome_curto = "sex"
        dis4.nome = "Sexta"
        dis4.save()
        
        dis5 = DiaSemana()
        dis5.nome_curto = "sab"
        dis5.nome = "Sabado"
        dis5.save()
        
        
        dis6 = DiaSemana()
        dis6.nome_curto = "dom"
        dis6.nome = "Domingo"
        dis6.save()