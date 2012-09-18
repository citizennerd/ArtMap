# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LifeEventType'
        db.create_table('artist_lifeeventtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('artist', ['LifeEventType'])

        # Adding model 'LifeEvent'
        db.create_table('artist_lifeevent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.Artist'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artist.LifeEventType'])),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('artist', ['LifeEvent'])

        # Adding model 'ArtistMeeting'
        db.create_table('artist_artistmeeting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('artist', ['ArtistMeeting'])

        # Adding M2M table for field artistLifeEvents on 'ArtistMeeting'
        db.create_table('artist_artistmeeting_artistLifeEvents', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('artistmeeting', models.ForeignKey(orm['artist.artistmeeting'], null=False)),
            ('lifeevent', models.ForeignKey(orm['artist.lifeevent'], null=False))
        ))
        db.create_unique('artist_artistmeeting_artistLifeEvents', ['artistmeeting_id', 'lifeevent_id'])

        # Deleting field 'Artist.death_date'
        db.delete_column('artist_artist', 'death_date')

        # Deleting field 'Artist.birth_date'
        db.delete_column('artist_artist', 'birth_date')

        # Adding field 'Art.artwork_link'
        db.add_column('artist_art', 'artwork_link',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Art.artwork_img'
        db.add_column('artist_art', 'artwork_img',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Art.wikipedia_link'
        db.add_column('artist_art', 'wikipedia_link',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'LifeEventType'
        db.delete_table('artist_lifeeventtype')

        # Deleting model 'LifeEvent'
        db.delete_table('artist_lifeevent')

        # Deleting model 'ArtistMeeting'
        db.delete_table('artist_artistmeeting')

        # Removing M2M table for field artistLifeEvents on 'ArtistMeeting'
        db.delete_table('artist_artistmeeting_artistLifeEvents')

        # Adding field 'Artist.death_date'
        db.add_column('artist_artist', 'death_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Artist.birth_date'
        db.add_column('artist_artist', 'birth_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Art.artwork_link'
        db.delete_column('artist_art', 'artwork_link')

        # Deleting field 'Art.artwork_img'
        db.delete_column('artist_art', 'artwork_img')

        # Deleting field 'Art.wikipedia_link'
        db.delete_column('artist_art', 'wikipedia_link')


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
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'artwork'", 'to': "orm['artist.Artist']"}),
            'artwork_img': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'artwork_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'creation_location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'relevantEntities': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artist.RelevantEntity']"}),
            'wikipedia_link': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'artist.artist': {
            'Meta': {'object_name': 'Artist'},
            'birth_location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'death_location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'artist.artistmeeting': {
            'Meta': {'object_name': 'ArtistMeeting'},
            'artistLifeEvents': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['artist.LifeEvent']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'artist.lifeevent': {
            'Meta': {'object_name': 'LifeEvent'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artist.Artist']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artist.LifeEventType']"})
        },
        'artist.lifeeventtype': {
            'Meta': {'object_name': 'LifeEventType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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