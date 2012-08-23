from django.contrib import admin
from project.jobs.models import *

class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'start', 'end', 'review', 'active']
    date_hierarchy = 'start'
    fieldsets = (
        ('Base Information', {'fields': ('title', 'link', 'description')}),
        ('Dates', {'fields': ('start', 'end', 'review')}),
        ('Meta', {'fields': ('active',)}),
    )

admin.site.register(JobListing, JobAdmin)