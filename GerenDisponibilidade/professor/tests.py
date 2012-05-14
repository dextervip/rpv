"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django_jenkins.runner import CITestSuiteRunner

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

"""
    def teste_view_vome(self):
        c = Client()
        response = c.get('/professor/')
        self.assertEqual(response.status_code, 200, "Ocorreu um erro.")
        self.assertTemplateUsed(response, "template_name", "msg_prefix")


    def teste_view_adicionarCompromisso(self):
        c = Client()
        response = c.get('/professor/adicionar-compromisso')
        self.assertEqual(response.status_code, 200, "Ocorreu um erro.")
        self.assertTemplateUsed(response, "template_name", "msg_prefix")
        
    def teste_view_editarCompromisso(self):
        c = Client()
        response = c.get('/professor/editar-compromisso/3')
        self.assertEqual(response.status_code, 200, "Ocorreu um erro.")
        self.assertTemplateUsed(response, "template_name", "msg_prefix")
        
        
    def teste_view_visualizarCompromisso(self):
        c = Client()
        response = c.get('/professor/visualizar-compromisso/3')
        self.assertEqual(response.status_code, 200, "Ocorreu um erro.")
        self.assertTemplateUsed(response, "template_name", "msg_prefix")
        
        
    def teste_view_excluirCompromisso(self):
        c = Client()
        response = c.get('/professor/visualizar-compromisso/4')
        self.assertEqual(response.status_code, 200, "Ocorreu um erro.")
        self.assertTemplateUsed(response, "template_name", "msg_prefix")
"""
