# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Extras.agency'
        db.alter_column(u'myapp_extras', 'agency', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Extras.unit_of_analysis'
        db.alter_column(u'myapp_extras', 'unit_of_analysis', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Extras.geographic_granularity'
        db.alter_column(u'myapp_extras', 'geographic_granularity', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Extras.collection_frequency'
        db.alter_column(u'myapp_extras', 'collection_frequency', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Extras.bureau_code'
        db.alter_column(u'myapp_extras', 'bureau_code', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Extras.author_id'
        db.alter_column(u'myapp_extras', 'author_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Extras.subject_area_1'
        db.alter_column(u'myapp_extras', 'subject_area_1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Relationship.relationship_description'
        db.alter_column(u'myapp_relationship', 'relationship_description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MedicalData.owner_org'
        db.alter_column(u'myapp_medicaldata', 'owner_org', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MedicalData.maintainer'
        db.alter_column(u'myapp_medicaldata', 'maintainer', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'MedicalData.maintainer_email'
        db.alter_column(u'myapp_medicaldata', 'maintainer_email', self.gf('django.db.models.fields.EmailField')(max_length=254, null=True))

        # Changing field 'MedicalData.author'
        db.alter_column(u'myapp_medicaldata', 'author', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MedicalData.author_email'
        db.alter_column(u'myapp_medicaldata', 'author_email', self.gf('django.db.models.fields.EmailField')(max_length=254, null=True))

        # Changing field 'MedicalData.state'
        db.alter_column(u'myapp_medicaldata', 'state', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MedicalData.version'
        db.alter_column(u'myapp_medicaldata', 'version', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MedicalData.license_id'
        db.alter_column(u'myapp_medicaldata', 'license_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MedicalData.type'
        db.alter_column(u'myapp_medicaldata', 'type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MedicalData.license_title'
        db.alter_column(u'myapp_medicaldata', 'license_title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MedicalData.name'
        db.alter_column(u'myapp_medicaldata', 'name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MedicalData.license'
        db.alter_column(u'myapp_medicaldata', 'license', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MedicalData.title'
        db.alter_column(u'myapp_medicaldata', 'title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MedicalData.ratings_average'
        db.alter_column(u'myapp_medicaldata', 'ratings_average', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MedicalData.organization'
        db.alter_column(u'myapp_medicaldata', 'organization', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MedicalData.revision_id'
        db.alter_column(u'myapp_medicaldata', 'revision_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Tag.tag_description'
        db.alter_column(u'myapp_tag', 'tag_description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Resource.mimetype'
        db.alter_column(u'myapp_resource', 'mimetype', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Resource.resource_group_id'
        db.alter_column(u'myapp_resource', 'resource_group_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Resource.hash'
        db.alter_column(u'myapp_resource', 'hash', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Resource.description'
        db.alter_column(u'myapp_resource', 'description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Resource.size'
        db.alter_column(u'myapp_resource', 'size', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Resource.format'
        db.alter_column(u'myapp_resource', 'format', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Resource.package_id'
        db.alter_column(u'myapp_resource', 'package_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Resource.mimetype_inner'
        db.alter_column(u'myapp_resource', 'mimetype_inner', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Resource.resource_type'
        db.alter_column(u'myapp_resource', 'resource_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Resource.name'
        db.alter_column(u'myapp_resource', 'name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Group.group_id'
        db.alter_column(u'myapp_group', 'group_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    def backwards(self, orm):

        # Changing field 'Extras.agency'
        db.alter_column(u'myapp_extras', 'agency', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Extras.unit_of_analysis'
        db.alter_column(u'myapp_extras', 'unit_of_analysis', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Extras.geographic_granularity'
        db.alter_column(u'myapp_extras', 'geographic_granularity', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Extras.collection_frequency'
        db.alter_column(u'myapp_extras', 'collection_frequency', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Extras.bureau_code'
        db.alter_column(u'myapp_extras', 'bureau_code', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Extras.author_id'
        db.alter_column(u'myapp_extras', 'author_id', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Extras.subject_area_1'
        db.alter_column(u'myapp_extras', 'subject_area_1', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Relationship.relationship_description'
        db.alter_column(u'myapp_relationship', 'relationship_description', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'MedicalData.owner_org'
        db.alter_column(u'myapp_medicaldata', 'owner_org', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'MedicalData.maintainer'
        db.alter_column(u'myapp_medicaldata', 'maintainer', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'MedicalData.maintainer_email'
        db.alter_column(u'myapp_medicaldata', 'maintainer_email', self.gf('django.db.models.fields.EmailField')(default='', max_length=254))

        # Changing field 'MedicalData.author'
        db.alter_column(u'myapp_medicaldata', 'author', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'MedicalData.author_email'
        db.alter_column(u'myapp_medicaldata', 'author_email', self.gf('django.db.models.fields.EmailField')(default='', max_length=254))

        # Changing field 'MedicalData.state'
        db.alter_column(u'myapp_medicaldata', 'state', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'MedicalData.version'
        db.alter_column(u'myapp_medicaldata', 'version', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'MedicalData.license_id'
        db.alter_column(u'myapp_medicaldata', 'license_id', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'MedicalData.type'
        db.alter_column(u'myapp_medicaldata', 'type', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'MedicalData.license_title'
        db.alter_column(u'myapp_medicaldata', 'license_title', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'MedicalData.name'
        db.alter_column(u'myapp_medicaldata', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'MedicalData.license'
        db.alter_column(u'myapp_medicaldata', 'license', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'MedicalData.title'
        db.alter_column(u'myapp_medicaldata', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'MedicalData.ratings_average'
        db.alter_column(u'myapp_medicaldata', 'ratings_average', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'MedicalData.organization'
        db.alter_column(u'myapp_medicaldata', 'organization', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'MedicalData.revision_id'
        db.alter_column(u'myapp_medicaldata', 'revision_id', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Tag.tag_description'
        db.alter_column(u'myapp_tag', 'tag_description', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Resource.mimetype'
        db.alter_column(u'myapp_resource', 'mimetype', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Resource.resource_group_id'
        db.alter_column(u'myapp_resource', 'resource_group_id', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Resource.hash'
        db.alter_column(u'myapp_resource', 'hash', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Resource.description'
        db.alter_column(u'myapp_resource', 'description', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Resource.size'
        db.alter_column(u'myapp_resource', 'size', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Resource.format'
        db.alter_column(u'myapp_resource', 'format', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Resource.package_id'
        db.alter_column(u'myapp_resource', 'package_id', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Resource.mimetype_inner'
        db.alter_column(u'myapp_resource', 'mimetype_inner', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Resource.resource_type'
        db.alter_column(u'myapp_resource', 'resource_type', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Resource.name'
        db.alter_column(u'myapp_resource', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Group.group_id'
        db.alter_column(u'myapp_group', 'group_id', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

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
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
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