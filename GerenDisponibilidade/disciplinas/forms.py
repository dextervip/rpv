# -*- encoding: utf-8 -*-

from django import forms
from models import newDisciplina

class FormNewDisciplina(forms.ModelForm):
    class Meta:
        model = newDisciplina
        