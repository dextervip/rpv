# -*- encoding: utf-8 -*-

from django import forms
from models import Compromisso

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class CadastroCompromisso(forms.Form):
    titulo = forms.CharField(label='Título', max_length=80, required=True)

    descricao = forms.CharField(label='Descrição',
        widget=forms.Textarea(),
    )
    
    dataInicio = forms.DateField(label='Data Início',)
    horaInicio = forms.TimeField(label='Hora Início', required=False)
    
    dataFim = forms.DateField(label='Data Fim',)
    horaFim = forms.TimeField(label='Hora Fim', help_text='<strong>Nota:</strong> Hora de finalização do compromisso.',required=False)
    
    diaInteiro = forms.BooleanField(label='Dia Inteiro',initial=False,required=False, help_text='Marque esta opção para compromisso não ter uma hora de início e fim.')

    publico = forms.MultipleChoiceField(label='Público', required=False,
        choices=(
            ('Público', 'Esta opção permite que todos tenhão acesso público para visualização deste compromisso'),
            
        ),
        widget=forms.CheckboxSelectMultiple,
        
        #help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    )
    
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
        
        FormActions(
            Submit('save_changes', 'Salvar', css_class="btn-primary"),
            Submit('cancel', 'Cancelar'),
        )
    )
    
 
