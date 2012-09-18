# -*- encoding: utf-8 -*-

from django import forms
from models import Disciplina


class FormNewDisciplina(forms.ModelForm):
    
    class Meta:
        model = Disciplina