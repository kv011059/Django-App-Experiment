from django.db import models

# Create your models here.
class Relationship(models.Model):
  relationship_description = models.CharField(max_length=50) # relationship_description is a made-up name

  def __unicode__(self):
    return u'%s' % (self.relationship_description)

class TrackingSummary(models.Model):
  total = models.DecimalField(max_digits=19, decimal_places=2)
  recent = models.DecimalField(max_digits=19, decimal_places=2)

  def __unicode__(self):
    return u'%5.3f %5.3f' % (self.total, self.recent)

class Tag(models.Model):
  tag_description = models.CharField(max_length=50) # tag_description is a made-up name

  def __unicode__(self):
    return u'%s' % (self.tag_description)

class Group(models.Model):
  group_id = models.CharField(max_length=50) # group_id is a made-up name

  def __unicode__(self):
    return u'%s' % (self.group_id)

class Resource(models.Model):
  resource_group_id = models.CharField(max_length=50)
  cache_last_updated = models.DateTimeField()
  package_id = models.CharField(max_length=50)
  webstore_last_updated = models.DateTimeField()
  id = models.CharField(primary_key=True, max_length=50)
  size = models.CharField(max_length=50)
  last_modified = models.DateTimeField()
  hash = models.CharField(max_length=50)
  description = models.CharField(max_length=50)
  format = models.CharField(max_length=50)
  tracking_summary = models.ForeignKey('TrackingSummary')
  mimetype_inner = models.CharField(max_length=50)
  mimetype = models.CharField(max_length=50)
  cache_url = models.URLField()
  name = models.CharField(max_length=50)
  created = models.DateTimeField()
  url = models.URLField()
  webstore_url = models.URLField()
  position = models.IntegerField()
  resource_type = models.CharField(max_length=50)

  def __unicode__(self):
    return u'%s %s' % (self.format, self.url)

class Extras(models.Model):
  coverage_period_start = models.DateTimeField()
  unit_of_analysis = models.CharField(max_length=50)
  hd2_workflow_id = models.IntegerField()
  agency = models.CharField(max_length=50)
  bureau_code = models.CharField(max_length=50)
  geographic_granularity = models.CharField(max_length=50)
  technical_documentation = models.TextField()
  collection_frequency = models.CharField(max_length=50)
  agency_program_url = models.URLField()
  date_updated = models.DateTimeField()
  date_released = models.DateTimeField()
  author_id = models.CharField(max_length=50)
  migration_notes_json = models.TextField()
  subject_area_1 = models.CharField(max_length=50)

  def __unicode__(self):
    return u'%s %d' % (self.agency, self.hd2_workflow_id)

class MedicalData(models.Model):
  license_title = models.CharField(max_length=50)
  maintainer = models.CharField(max_length=100)
  private = models.BooleanField()
  maintainer_email = models.EmailField(max_length=254)
  num_tags = models.PositiveSmallIntegerField()
  id = models.CharField(primary_key=True, max_length=50)
  metadata_created = models.DateTimeField()
  relationships = models.ManyToManyField(Relationship) # assume relationships is an array of string
  license = models.CharField(max_length=50)
  metadata_modified = models.DateTimeField()
  author = models.CharField(max_length=50)
  author_email = models.EmailField(max_length=254)
  state = models.CharField(max_length=50)
  version = models.CharField(max_length=50)
  license_id = models.CharField(max_length=50)
  type = models.CharField(max_length=50)
  resources = models.ManyToManyField(Resource)
  num_resources = models.PositiveSmallIntegerField()
  tags = models.ManyToManyField(Tag)
  tracking_summary = models.ForeignKey('TrackingSummary')
  groups = models.ManyToManyField(Group)
  organization = models.CharField(max_length=50)
  name = models.CharField(max_length=50)
  isopen = models.BooleanField()
  notes_rendered = models.TextField()
  url = models.URLField()
  ckan_url = models.URLField()
  notes = models.TextField()
  owner_org = models.CharField(max_length=50)
  ratings_average = models.CharField(max_length=50)
  extras = models.ForeignKey('Extras')
  ratings_count = models.PositiveSmallIntegerField()
  title = models.CharField(max_length=50)
  revision_id = models.CharField(max_length=50)
  
  def __unicode__(self):
    return u'%s %s' % (self.license_title, self.author)

