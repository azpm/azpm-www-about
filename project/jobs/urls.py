from django.conf.urls import *

urlpatterns = patterns('project.jobs.views',
    url(r'^$', 'index', name = 'job-listings'),
)
