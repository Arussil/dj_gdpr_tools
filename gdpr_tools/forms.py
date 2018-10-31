from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Consent, Category
from .utils import get_ip


class ConsentForm(forms.Form):
    CHOICES = (
        (True, _('Accept')),
        (False, _('Refuse')),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ConsentForm, self).__init__(*args, **kwargs)
        for category in Category.objects.get_facultative_categories():
            self.fields[category.name] = forms.ChoiceField(
                choices=self.CHOICES,
                widget=forms.RadioSelect
            )

    def save(self):
        for category in self.cleaned_data:
            category = Category.objects.get(name=category)
            consent = Consent(
                category=category,
                ip = get_ip(self.request),
                accepted = self.cleaned_data[category.name]
            )
            consent.save()
