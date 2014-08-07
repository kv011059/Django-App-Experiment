from django.contrib import admin

from myapp.models import MedicalData

class MDAdmin(admin.ModelAdmin):
  fields = ['metadata_created', 'maintainer']
  list_display = ('metadata_created', 'maintainer')
  list_filter = ['metadata_created']
  search_fields = ['metadata_created']

admin.site.register(MedicalData, MDAdmin)

