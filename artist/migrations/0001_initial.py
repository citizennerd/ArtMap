# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table('artist_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('death_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('birth_location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('death_location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal('artist', ['Artist'])

        # Adding model 'Alias'
        db.create_table('artist_alias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(related_name='aliases', to=orm['artist.Artist'])),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PolygonField')(null=True, blank=True)),
            ('timeend', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('timestart', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('artist', ['Alias'])

        # Adding model 'Art'
        db.create_table('artist_art', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.Artist'])),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('creation_location', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('relevantEntities', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.RelevantEntity'])),
        ))
        db.send_create_signal('artist', ['Art'])

        # Adding model 'RelevantEntity'
        db.create_table('artist_relevantentity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('area', self.gf('django.contrib.gis.db.models.fields.PolygonField')(null=True, blank=True)),
            ('position', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal('artist', ['RelevantEntity'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table('artist_artist')

        # Deleting model 'Alias'
        db.delete_table('artist_alias')

        # Deleting model 'Art'
        db.delete_table('artist_art')

        # Deleting model 'RelevantEntity'
        db.delete_table('artist_relevantentity')


    models = {
        'artist.alias': {
            'Meta': {'object_name': 'Alias'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'aliases'", 'to': "orm['artist.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True', 'blank': 'True'}),
            'timeend': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'timestart': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
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
        }
    }

    complete_apps = ['artist']