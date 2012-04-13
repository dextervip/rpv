# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from unittest import TestSuite
from django.test.client import Client
from django_jenkins.runner import CITestSuiteRunner


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class TestFirstView(TestCase):
    def test_first_view(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200, "Ocorreu um erro.")
        self.assertEqual(response.content, "Ola, este é um teste do django", response.content + "A resposta nao eh a esperada.")
