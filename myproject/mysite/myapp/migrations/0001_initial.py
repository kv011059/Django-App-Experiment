# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Relationship'
        db.create_table(u'myapp_relationship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('relationship_description', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'myapp', ['Relationship'])

        # Adding model 'TrackingSummary'
        db.create_table(u'myapp_trackingsummary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
            ('recent', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=2)),
        ))
        db.send_create_signal(u'myapp', ['TrackingSummary'])

        # Adding model 'Tag'
        db.create_table(u'myapp_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_description', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'myapp', ['Tag'])

        # Adding model 'Group'
        db.create_table(u'myapp_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'myapp', ['Group'])

        # Adding model 'Resource'
        db.create_table(u'myapp_resource', (
            ('resource_group_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cache_last_updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('package_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('webstore_last_updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')()),
            ('hash', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tracking_summary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myapp.TrackingSummary'])),
            ('mimetype_inner', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('mimetype', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cache_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('webstore_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('resource_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'myapp', ['Resource'])

        # Adding model 'Extras'
        db.create_table(u'myapp_extras', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coverage_period_start', self.gf('django.db.models.fields.DateTimeField')()),
            ('unit_of_analysis', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('hd2_workflow_id', self.gf('django.db.models.fields.IntegerField')()),
            ('agency', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('bureau_code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('geographic_granularity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('technical_documentation', self.gf('django.db.models.fields.TextField')()),
            ('collection_frequency', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('agency_program_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_released', self.gf('django.db.models.fields.DateTimeField')()),
            ('author_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('migration_notes_json', self.gf('django.db.models.fields.TextField')()),
            ('subject_area_1', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'myapp', ['Extras'])

        # Adding model 'MedicalData'
        db.create_table(u'myapp_medicaldata', (
            ('license_title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('maintainer', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('private', self.gf('django.db.models.fields.BooleanField')()),
            ('maintainer_email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('num_tags', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('metadata_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('license', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('metadata_modified', self.gf('django.db.models.fields.DateTimeField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('author_email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('license_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('num_resources', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('tracking_summary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myapp.TrackingSummary'])),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('isopen', self.gf('django.db.models.fields.BooleanField')()),
            ('notes_rendered', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('ckan_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('owner_org', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ratings_average', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('extras', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myapp.Extras'])),
            ('ratings_count', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('revision_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'myapp', ['MedicalData'])

        # Adding M2M table for field relationships on 'MedicalData'
        m2m_table_name = db.shorten_name(u'myapp_medicaldata_relationships')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('medicaldata', models.ForeignKey(orm[u'myapp.medicaldata'], null=False)),
            ('relationship', models.ForeignKey(orm[u'myapp.relationship'], null=False))
        ))
        db.create_unique(m2m_table_name, ['medicaldata_id', 'relationship_id'])

        # Adding M2M table for field resources on 'MedicalData'
        m2m_table_name = db.shorten_name(u'myapp_medicaldata_resources')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('medicaldata', models.ForeignKey(orm[u'myapp.medicaldata'], null=False)),
            ('resource', models.ForeignKey(orm[u'myapp.resource'], null=False))
        ))
        db.create_unique(m2m_table_name, ['medicaldata_id', 'resource_id'])

        # Adding M2M table for field tags on 'MedicalData'
        m2m_table_name = db.shorten_name(u'myapp_medicaldata_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('medicaldata', models.ForeignKey(orm[u'myapp.medicaldata'], null=False)),
            ('tag', models.ForeignKey(orm[u'myapp.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['medicaldata_id', 'tag_id'])

        # Adding M2M table for field groups on 'MedicalData'
        m2m_table_name = db.shorten_name(u'myapp_medicaldata_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('medicaldata', models.ForeignKey(orm[u'myapp.medicaldata'], null=False)),
            ('group', models.ForeignKey(orm[u'myapp.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['medicaldata_id', 'group_id'])


    def backwards(self, orm):
        # Deleting model 'Relationship'
        db.delete_table(u'myapp_relationship')

        # Deleting model 'TrackingSummary'
        db.delete_table(u'myapp_trackingsummary')

        # Deleting model 'Tag'
        db.delete_table(u'myapp_tag')

        # Deleting model 'Group'
        db.delete_table(u'myapp_group')

        # Deleting model 'Resource'
        db.delete_table(u'myapp_resource')

        # Deleting model 'Extras'
        db.delete_table(u'myapp_extras')

        # Deleting model 'MedicalData'
        db.delete_table(u'myapp_medicaldata')

        # Removing M2M table for field relationships on 'MedicalData'
        db.delete_table(db.shorten_name(u'myapp_medicaldata_relationships'))

        # Removing M2M table for field resources on 'MedicalData'
        db.delete_table(db.shorten_name(u'myapp_medicaldata_resources'))

        # Removing M2M table for field tags on 'MedicalData'
        db.delete_table(db.shorten_name(u'myapp_medicaldata_tags'))

        # Removing M2M table for field groups on 'MedicalData'
        db.delete_table(db.shorten_name(u'myapp_medicaldata_groups'))


    models = {
        u'myapp.extras': {
            'Meta': {'object_name': 'Extras'},
            'agency': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'agency_program_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'author_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'bureau_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'collection_frequency': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'coverage_period_start': ('django.db.models.fields.DateTimeField', [], {}),
            'date_released': ('django.db.models.fields.DateTimeField', [], {}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'geographic_granularity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hd2_workflow_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'migration_notes_json': ('django.db.models.fields.TextField', [], {}),
            'subject_area_1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'technical_documentation': ('django.db.models.fields.TextField', [], {}),
            'unit_of_analysis': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'myapp.group': {
            'Meta': {'object_name': 'Group'},
            'group_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'myapp.medicaldata': {
            'Meta': {'object_name': 'MedicalData'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'ckan_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'extras': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myapp.Extras']"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['myapp.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'isopen': ('django.db.models.fields.BooleanField', [], {}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'license_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'license_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'maintainer': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'maintainer_email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'metadata_created': ('django.db.models.fields.DateTimeField', [], {}),
            'metadata_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'notes_rendered': ('django.db.models.fields.TextField', [], {}),
            'num_resources': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'num_tags': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner_org': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'private': ('django.db.models.fields.BooleanField', [], {}),
            'ratings_average': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ratings_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'relationships': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['myapp.Relationship']", 'symmetrical': 'False'}),
            'resources': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['myapp.Resource']", 'symmetrical': 'False'}),
            'revision_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['myapp.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tracking_summary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myapp.TrackingSummary']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'myapp.relationship': {
            'Meta': {'object_name': 'Relationship'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship_description': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'myapp.resource': {
            'Meta': {'object_name': 'Resource'},
            'cache_last_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'cache_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {}),
            'mimetype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mimetype_inner': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'package_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'resource_group_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'resource_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tracking_summary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myapp.TrackingSummary']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'webstore_last_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'webstore_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'myapp.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_description': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'myapp.trackingsummary': {
            'Meta': {'object_name': 'TrackingSummary'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recent': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'})
        }
    }

    complete_apps = ['myapp']