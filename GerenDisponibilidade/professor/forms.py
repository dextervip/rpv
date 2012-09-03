# -*- encoding: utf-8 -*-

from django import forms
from models import Compromisso, DiaSemana

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.templatetags.crispy_forms_field import css_class

import datetime

class CadastroCompromisso(forms.ModelForm):
    
    titulo = forms.CharField(label='Título', max_length=80, required=True)

    descricao = forms.CharField(label='Descrição',
        widget=forms.Textarea(),
    )
    
    dataInicio = forms.DateField(label='Data Início', initial=datetime.date.today)
    horaInicio = forms.TimeField(label='Hora Início', required=False)
    
    dataFim = forms.DateField(label='Data Fim', initial=datetime.date.today)
    horaFim = forms.TimeField(label='Hora Fim', help_text='<strong>Nota:</strong> Hora de finalização do compromisso.', required=False)
    
    diaInteiro = forms.BooleanField(label='Dia Inteiro', initial=False, required=False, help_text='Marque esta opção para compromisso não ter uma hora de início e fim.')

    publico = forms.BooleanField(label='Público',
                                 initial=False,
                                 required=False,
                                 help_text='Esta opção permite que todos tenhão acesso público para visualização deste compromisso',
    )
    
    frequencia = forms.TypedChoiceField(label='Frequência', choices=(
                                                                (0, 'Apenas Uma vez'),
                                                                (1, 'Todos os Dias'),
                                                                (2, 'Semanal'),
                                                                (3, 'Mensal'),
                                                                #(4, 'Semestral'),
                                                                (5, 'Anual')
                                                                ), widget=forms.RadioSelect, initial=0, required=True,)
    #É necessário mudar-se o tipo do form, se quiser que aceite dados nullos.
    dataFimFrequencia = forms.DateField(label='Fim da Frequência')
    
    diaSemana = forms.MultipleChoiceField(label='Dias da Semana', choices=DiaSemana.DIAS_CHOICES, initial="0", widget=forms.CheckboxSelectMultiple, required=False) 
    
    
    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('titulo', css_class='input-xxlarge'),
        Field('descricao', rows='8', css_class='input-xxlarge'),
        
        Field('dataInicio', css_class='input-xlarge datapicker'),
        Field('horaInicio', css_class='input-xlarge horas'),
        
        Field('dataFim', css_class='input-xlarge datapicker'),
        Field('horaFim', css_class='input-xlarge horas'),
  
        Field('diaInteiro', id='diaInteiro'),
          
        Field('publico', style="background: #FAFAFA; padding: 10px;"),
        
        Field('frequencia', id='frequencia'),
        
        Field('dataFimFrequencia', css_class='input-xlarge datapicker'),
        
        Field('diaSemana', id='diaSemana'),
        
        FormActions(
            Submit('save_changes', 'Salvar', css_class="btn btn-success btn-large"),
            HTML('<span> <a href="{% url professor:home %}" class="btn btn-danger btn-large excluir">&laquo;  Descartar </a> </span>'),
        )
    )
    
    class Meta:
        model = Compromisso
    
 
