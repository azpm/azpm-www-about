from django.conf.urls import *

urlpatterns = patterns('project.contact.views',
    url(r'^thanks/$', 'thanks', name="thanks"),
    url(r'^(?P<username>[\w-]+)/$', 'person', name="contact-person"),
    url(r'^$', 'index', name="contact-main")
)
