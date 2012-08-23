from django.conf.urls import *
from django.contrib import admin
from libscampi.contrib import cms

admin.autodiscover()

urlpatterns = patterns('',
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^people/', include('libazpm.contrib.people.urls')),
    (r'^contact/', include('project.contact.urls', namespace="contact")),
    (r'^jobs/', include('project.jobs.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^admin/', include(admin.site.urls)),
    (r'', include(cms.site.urls)) 
)
