# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MedicalData.id'
        db.alter_column(u'myapp_medicaldata', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

        # Changing field 'Resource.id'
        db.alter_column(u'myapp_resource', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

    def backwards(self, orm):

        # Changing field 'MedicalData.id'
        db.alter_column(u'myapp_medicaldata', 'id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True))

        # Changing field 'Resource.id'
        db.alter_column(u'myapp_resource', 'id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True))

    models = {
        u'myapp.extras': {
            'Meta': {'object_name': 'Extras'},
            'agency': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'agency_program_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'author_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'bureau_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'collection_frequency': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'coverage_period_start': ('django.db.models.fields.DateTimeField', [], {}),
            'date_released': ('django.db.models.fields.DateTimeField', [], {}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'geographic_granularity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'hd2_workflow_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'migration_notes_json': ('django.db.models.fields.TextField', [], {}),
            'subject_area_1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'technical_documentation': ('django.db.models.fields.TextField', [], {}),
            'unit_of_analysis': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'myapp.group': {
            'Meta': {'object_name': 'Group'},
            'group_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'myapp.medicaldata': {
            'Meta': {'object_name': 'MedicalData'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'ckan_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'extras': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myapp.Extras']"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['myapp.Group']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isopen': ('django.db.models.fields.BooleanField', [], {}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'license_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'license_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'maintainer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'maintainer_email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'metadata_created': ('django.db.models.fields.DateTimeField', [], {}),
            'metadata_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'notes_rendered': ('django.db.models.fields.TextField', [], {}),
            'num_resources': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'num_tags': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'owner_org': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'private': ('django.db.models.fields.BooleanField', [], {}),
            'ratings_average': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ratings_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'relationships': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['myapp.Relationship']", 'symmetrical': 'False'}),
            'resources': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['myapp.Resource']", 'symmetrical': 'False'}),
            'revision_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['myapp.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tracking_summary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myapp.TrackingSummary']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'myapp.relationship': {
            'Meta': {'object_name': 'Relationship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship_description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'myapp.resource': {
            'Meta': {'object_name': 'Resource'},
            'cache_last_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'cache_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'mimetype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'mimetype_inner': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'package_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'resource_group_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'resource_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tracking_summary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myapp.TrackingSummary']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'webstore_last_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'webstore_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'myapp.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'myapp.trackingsummary': {
            'Meta': {'object_name': 'TrackingSummary'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recent': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'})
        }
    }

    complete_apps = ['myapp']