# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Compromisso'
        db.create_table('professor_compromisso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('descricao', self.gf('django.db.models.fields.TextField')()),
            ('dataInicio', self.gf('django.db.models.fields.DateField')()),
            ('dataFim', self.gf('django.db.models.fields.DateField')()),
            ('horaInicio', self.gf('django.db.models.fields.DateField')()),
            ('horaFim', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('professor', ['Compromisso'])

    def backwards(self, orm):
        # Deleting model 'Compromisso'
        db.delete_table('professor_compromisso')

    models = {
        'professor.compromisso': {
            'Meta': {'object_name': 'Compromisso'},
            'dataFim': ('django.db.models.fields.DateField', [], {}),
            'dataInicio': ('django.db.models.fields.DateField', [], {}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'horaFim': ('django.db.models.fields.DateField', [], {}),
            'horaInicio': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['professor']