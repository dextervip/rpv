# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'newDisciplina'
        db.create_table('disciplinas_newdisciplina', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('curso', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('campus', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('cargaHora', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('creditosPraticos', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('creditosTeoricos', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('anoLetivo', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('turno', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('turma', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('ementa', self.gf('django.db.models.fields.TextField')()),
            ('objetivoGeral', self.gf('django.db.models.fields.TextField')()),
            ('objetivoEspecif', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('preRequisitos', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('bibliograBasica', self.gf('django.db.models.fields.TextField')()),
            ('bibliograComplem', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('disciplinas', ['newDisciplina'])

    def backwards(self, orm):
        # Deleting model 'newDisciplina'
        db.delete_table('disciplinas_newdisciplina')

    models = {
        'disciplinas.newdisciplina': {
            'Meta': {'object_name': 'newDisciplina'},
            'anoLetivo': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'bibliograBasica': ('django.db.models.fields.TextField', [], {}),
            'bibliograComplem': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'campus': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'cargaHora': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'creditosPraticos': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'creditosTeoricos': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'curso': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'ementa': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'objetivoEspecif': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'objetivoGeral': ('django.db.models.fields.TextField', [], {}),
            'preRequisitos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'turma': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'turno': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['disciplinas']