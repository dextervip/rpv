# -*- encoding: utf-8 -*-
from django import forms
from models import TipoDeSala
from models import Sala
from django.utils.safestring import mark_safe


class FormTipoDeSala(forms.ModelForm):
    class Meta:
        model = TipoDeSala
    
#Add Marcação de Campo Obrigatorio, nos forms || Fonte: http://blog.gustavohenrique.net/2009/05/colocando-um-asterisco-no-label-dos-campos-obrigatorios/
    def __init__(self, *args, **kwargs):
        for campo in self.base_fields:
            if self.base_fields[campo].required:
                self.base_fields[campo].label = mark_safe('<span style="color:red;">*</span> %s' % self.base_fields[campo].label)
        super(FormTipoDeSala, self).__init__(*args, **kwargs)


class FormSala(forms.ModelForm):
    class Meta:
        model = Sala
    
#Add Marcação de Campo Obrigatorio, nos forms || Fonte: http://blog.gustavohenrique.net/2009/05/colocando-um-asterisco-no-label-dos-campos-obrigatorios/
    def __init__(self, *args, **kwargs):
        for campo in self.base_fields:
            if self.base_fields[campo].required:
                self.base_fields[campo].label = mark_safe('<span style="color:red;">*</span> %s' % self.base_fields[campo].label)
        super(FormSala, self).__init__(*args, **kwargs)