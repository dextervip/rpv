# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django_jenkins.runner import CITestSuiteRunner


class TestClass(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
""" 
    def test_first_view(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200, "Ocorreu um erro.")
        #self.assertEqual(response.content, "Olá",  "Resposta não esperada")
"""