from project.jobs.models import JobListing
from datetime import datetime

from libscampi.contrib.cms.views.base import Page
from libscampi.contrib.cms.communism.models import *
from django.conf import settings

class JobsPage(Page):
    base_title = u"Employment Opportunities"
    cached_css_key = 'jobs:css'
    cached_js_key = 'jobs:js'

    jobs_css = {
        'url': "%sintensifier/css/job_listings.css" % settings.STATIC_URL,
        'media': "screen",
        'for_ie': False
    }

    def get_static_styles(self):
        return [self.jobs_css]

    def get_theme(self):
        try:
            theme = Theme.objects.get(keyname="intensifier")
        except Theme.DoesNotExist:
            theme = Theme.objects.none()

        return theme

    def get_page_title(self):
        return self.base_title

class Index(JobsPage):
    template_name = 'jobs/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)

        jobs = JobListing.objects.filter(active = True).order_by('-start').exclude(end__lte=datetime.today(), end__isnull=False)

        c = {
            'jobs': jobs
        }

        context.update(c)

        return context