# -*- encoding: utf-8 -*-

from professor.models import Professor, AreaFormacao

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
        af1 = AreaFormacao()
        af1.nome = "Computação"
        af1.save()
        
        af2 = AreaFormacao()
        af2.nome = "Engenharia Civil"
        af2.save()
        
        af3 = AreaFormacao()
        af3.nome = "Engenharia de Software"
        af3.save()
        
        p = Professor()
        p.nome = "João Pablo"
        p.save()
        p.areaFormacao.add(af1)
        p.areaFormacao.add(af3)
        p.save()