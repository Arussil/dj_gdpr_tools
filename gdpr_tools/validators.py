import os

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


#TODO: migliorare il riconoscimento del file per evitare rischi di sicurezza
def validate_file_extension(value):
    ext = os.path.splitext(value.name[1])
    valid_extensions = ['.js']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Only JS file allowed'))
