# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Museum'
        db.create_table('museum_museum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('position', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal('museum', ['Museum'])

        # Adding model 'CollectedArtwork'
        db.create_table('museum_collectedartwork', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artwork', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.Art'])),
            ('museum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['museum.Museum'])),
        ))
        db.send_create_signal('museum', ['CollectedArtwork'])


    def backwards(self, orm):
        # Deleting model 'Museum'
        db.delete_table('museum_museum')

        # Deleting model 'CollectedArtwork'
        db.delete_table('museum_collectedartwork')


    models = {
        'artist.art': {
            'Meta': {'object_name': 'Art'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artist.Artist']"}),
            'creation_location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'relevantEntities': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artist.RelevantEntity']"})
        },
        'artist.artist': {
            'Meta': {'object_name': 'Artist'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'birth_location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'death_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'death_location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'artist.relevantentity': {
            'Meta': {'object_name': 'RelevantEntity'},
            'area': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.contrib.gis.db.models.fields.PointField', [], {})
        },
        'museum.collectedartwork': {
            'Meta': {'object_name': 'CollectedArtwork'},
            'artwork': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artist.Art']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'museum': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['museum.Museum']"})
        },
        'museum.museum': {
            'Meta': {'object_name': 'Museum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'position': ('django.contrib.gis.db.models.fields.PointField', [], {})
        }
    }

    complete_apps = ['museum']