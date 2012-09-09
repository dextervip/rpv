"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from professor.models import Professor, DiaSemana, DisponibilidadeAula

class SimpleTest(TestCase):
        
    def adicionaDisponibilidade(self):
        p = Professor.objects.get(id=1)
        
        ds = DiaSemana.objects.get(nome_curto="qua");
        dis, created = DisponibilidadeAula.objects.get_or_create(hora="14:30")
        if created == True:
            dis.hora = "14:30"
            dis.save()
        dis.diaSemana=ds
        dis.save()
        
        p.disponibilidadeAula.add(dis)
        p.save()
        
        result = p.getDisponibilidadeAula("qua","14:30")
        self.assertEqual(result, dis)