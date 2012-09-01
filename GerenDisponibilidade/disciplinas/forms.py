# -*- encoding: utf-8 -*-

from django import forms
from models import Disciplina

"""
# Importamos o metodo mark_safe que possibilita utilizar códigos html
from django.utils.safestring import mark_safe
"""

class FormNewDisciplina(forms.ModelForm):
    
    class Meta:
        model = Disciplina

"""      
#Add Marcação de Campo Obrigatorio, nos forms || Fonte: http://blog.gustavohenrique.net/2009/05/colocando-um-asterisco-no-label-dos-campos-obrigatorios/
    def __init__(self, *args, **kwargs):
        for campo in self.base_fields:
            if self.base_fields[campo].required:
                self.base_fields[campo].label = mark_safe('<span style="color:red;">*</span> %s' % self.base_fields[campo].label)
        super(FormNewDisciplina, self).__init__(*args, **kwargs)
"""
