# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Map'
        db.create_table('mapper_map', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('author', self.gf('django.db.models.fields.CharField')(default='Unknown', max_length=250, null=True, blank=True)),
            ('origin', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('mapper', ['Map'])

        # Adding model 'GeoLocation'
        db.create_table('mapper_geolocation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mapper.Map'])),
            ('BB_left', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('BB_top', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('BB_right', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('BB_bottom', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('rotation', self.gf('django.db.models.fields.FloatField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal('mapper', ['GeoLocation'])


    def backwards(self, orm):
        # Deleting model 'Map'
        db.delete_table('mapper_map')

        # Deleting model 'GeoLocation'
        db.delete_table('mapper_geolocation')


    models = {
        'mapper.geolocation': {
            'BB_bottom': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'BB_left': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'BB_right': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'BB_top': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'GeoLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mapper.Map']"}),
            'rotation': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        'mapper.map': {
            'Meta': {'object_name': 'Map'},
            'author': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'origin': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mapper']