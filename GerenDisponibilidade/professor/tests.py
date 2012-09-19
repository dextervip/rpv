"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from professor.models import Professor, DiaSemana, DisponibilidadeAula
from professor.models import Professor, DiaSemana, DisponibilidadeAula 
 

class SimpleTest(TestCase):
        
    def adicionaDisponibilidade(self):
        p = Professor.objects.get(id=1)
        p.informarDisponibilidade("qua", "14:30")
        
        p = Professor.objects.get(id=1)
        result = p.getDisponibilidadeAulas()
        
        self.assertEqual(result[0].hora, "14:30")
        self.assertEqual(result[0].diaSemana.nome_curto, "qua")
        self.assertEqual(result[0].diaSemana.nome_curto, "quar")