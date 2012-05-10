# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Compromisso.horaFim'
        db.alter_column('professor_compromisso', 'horaFim', self.gf('django.db.models.fields.TimeField')())

        # Changing field 'Compromisso.horaInicio'
        db.alter_column('professor_compromisso', 'horaInicio', self.gf('django.db.models.fields.TimeField')())
    def backwards(self, orm):

        # Changing field 'Compromisso.horaFim'
        db.alter_column('professor_compromisso', 'horaFim', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Compromisso.horaInicio'
        db.alter_column('professor_compromisso', 'horaInicio', self.gf('django.db.models.fields.DateField')())
    models = {
        'professor.compromisso': {
            'Meta': {'object_name': 'Compromisso'},
            'dataFim': ('django.db.models.fields.DateTimeField', [], {}),
            'dataInicio': ('django.db.models.fields.DateTimeField', [], {}),
            'descricao': ('django.db.models.fields.TextField', [], {}),
            'horaFim': ('django.db.models.fields.TimeField', [], {}),
            'horaInicio': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['professor']