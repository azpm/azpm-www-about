from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from libscampi.contrib.cms.admin import cms_admin as about_admin

from libazpm.contrib.people.models import *
from libazpm.contrib.people.admin import *
from project.jobs.admin import JobAdmin
from project.jobs.models import JobListing
from project.advisoryboard.admin import PABMeetingAdmin, PABNewsAdmin
from project.advisoryboard.models import PABMeeting, PABNews

about_admin.register(JobListing, JobAdmin)
about_admin.register(PABMeeting, PABMeetingAdmin)
about_admin.register(PABNews, PABNewsAdmin)

about_admin.register(Person, PersonAdmin)
about_admin.register(AZPMGroup, AZPMGroupAdmin)
about_admin.register(FeaturedPerson, FeaturedPeopleAdmin)

about_admin.register(User, UserAdmin)