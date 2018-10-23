from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import validate_file_extension


class Category(models.Model):
    """
    Category of the Cookie.
    es. Marketing/Statistics
    """
    NECESSARY = 'NE'
    FACULTATIVE = 'FA'
    CATEGORY_TYPE_CHOICES = (
        (NECESSARY, _('Necessary')),
        (FACULTATIVE, _('Facultative')),
    )
    name = models.CharField(_('Name'), max_length=100, unique=True)
    type = models.CharField(
        _('Type'),
        max_length=2,
        choices=CATEGORY_TYPE_CHOICES
    )

    class Meta():
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

class Cookie(models.Model):
    """
    Register cookie and his code (a js file)
    """
    name = models.CharField(_('Name'), max_length=100)
    category = models.ForeignKey(
        Category,
        verbose_name = _('Category'),
        on_delete = models.CASCADE,
        related_name = 'cookies',
    )
    file = models.FileField(
        upload_to='cookie_scripts',
        validators=[validate_file_extension],
        blank=True,
    )

    class Meta():
        verbose_name = _('Cookie')
        verbose_name_plural = _('Cookies')

    def __str__(self):
        return self.name

class Consent(models.Model):
    """
    Register user consent for Cookie Category
    Using IP to store it so we can match
    with third party like analytics and Facebook
    """
    category = models.ForeignKey(
        Category,
        verbose_name = _('Category'),
        on_delete = models.CASCADE,
        related_name = 'consents',
    )
    ip = models.GenericIPAddressField()
    accepted = models.BooleanField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = _('Consent')
        verbose_name_plural = _('Consents')

    def __str__(self):
        return self.ip
