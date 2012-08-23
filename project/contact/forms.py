from django import forms
from django.contrib.localflavor.us.forms import USPhoneNumberField

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 200)
    email = forms.EmailField(help_text = u"We value your privacy and will only use your email to respond to your inquiry")
    phone = USPhoneNumberField(required = False, help_text = u"xxx-xxx-xxxx")
    address = forms.CharField(widget = forms.widgets.Textarea, required = False)
    subject = forms.CharField(max_length = 200, help_text = u"What are you contacting us about?")
    message = forms.CharField(widget = forms.widgets.Textarea)
    honeypot = forms.CharField(required=False, label='If you enter anything in this field '\
                'your comment will be treated as spam')

    def clean_honeypot(self):
        """Check that nothing's been entered into the honeypot."""
        value = self.cleaned_data["honeypot"]
        if value:
            raise forms.ValidationError(self.fields["honeypot"].label)
        return value