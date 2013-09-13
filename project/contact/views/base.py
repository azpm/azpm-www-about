import logging
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import FormView
from libscampi.contrib.cms.views.base import Page
from project.contact.forms import ContactForm
from django.contrib import messages

logger = logging.getLogger("project.contact.views")

class ContactPage(Page):
    base_title = u"Contact"
    cached_css_key = "about:contact:css"
    cached_js_key = "about:contact:js"

    def get_theme(self):
        return self.realm.theme

    def get_page_title(self):
        return self.base_title

class Index(ContactPage, FormView):
    form_class = ContactForm
    template_name = "contact/index.html"

    def post(self, request, *args, **kwargs):
        return super(Index, self).post(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)

        if "form" not in kwargs:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
        else:
            form = kwargs.get('form')

        c = {'form': form}
        context.update(c)

        return context

    def form_valid(self, form):
        cleaned = form.cleaned_data
        message_context = {
            'name': cleaned['name'],
            'subject': cleaned['subject'],
            'message': cleaned['message'],
            'phone': cleaned['phone'],
            'address': cleaned['address'],
            'useragent': self.request.META.get('HTTP_USER_AGENT', ''),
            'userip': self.request.META.get('REMOTE_ADDR',''),
            'email': cleaned['email']
        }

        email_body = render_to_string('contact/contact.email.txt', message_context)
        email = EmailMessage(
            subject = 'about.azpm.org Feedback',
            body =  email_body,
            from_email =  'postoffice@azpm.org',
            to = ['cu@azpm.org'],
            headers = {'Reply-To': "%s <%s>" % (cleaned['name'], cleaned['email'])},
        )
        email.send()
        messages.success(self.request, "Thanks for your feedback. We will process your comments and make sure they are heard!")
        return HttpResponseRedirect(reverse("contact:thanks"))

class ContactPerson(ContactPage, FormView):
    contact_user = None
    form_class = ContactForm
    template_name = "contact/contact_person.html"

    def get(self, request, *args, **kwargs):
        self.contact_user = get_object_or_404(User, username = kwargs['username'])

        return super(ContactPerson, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.contact_user = get_object_or_404(User, username = kwargs['username'])

        return super(ContactPerson, self).post(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(ContactPerson, self).get_context_data(*args, **kwargs)

        if "form" not in kwargs:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
        else:
            form = kwargs.get('form')

        c = {'form': form, 'contact_user': self.contact_user}
        context.update(c)

        return context

    def form_valid(self, form):
        cleaned = form.cleaned_data

        message_context = {
            'name': cleaned['name'],
            'subject': cleaned['subject'],
            'message': cleaned['message'],
            'phone': cleaned['phone'],
            'address': cleaned['address'],
            'useragent': self.request.META.get('HTTP_USER_AGENT', ''),
            'userip': self.request.META.get('REMOTE_ADDR','')
        }

        email_body = render_to_string('contact/contact.email.txt', message_context)
        email = EmailMessage(
            subject = 'about.azpm.org Feedback',
            body =  email_body,
            from_email =  'postoffice@azpm.org',
            to = [self.contact_user.email],
            headers = {'Reply-To': "%s <%s>" % (cleaned['name'], cleaned['email'])},
        )
        email.send()
        messages.success(self.request, "Thanks for your feedback. We will process your comments and make sure they are heard!")
        return HttpResponseRedirect(reverse("contact:thanks"))

    def get_page_title(self):
        return u"Contact {0:>s}".format(self.contact_user.get_full_name())

class Thanks(ContactPage):
    template_name = 'contact/thanks.html'

    def get_page_title(self):
        return "Thank you for your feedback"