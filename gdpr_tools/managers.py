from django.apps import apps
from django.db import models
from django.db.models import Prefetch


class CategoryManager(models.Manager):
    def get_facultative_categories(self):
        """
        All active facultative category with
        at least one active cookie
        """
        return self.filter(
            type=self.model.FACULTATIVE,
            active=True,
            cookies__active=True,
        ).distinct()

    def get_facultative_categories_and_cookies(self):
        """
        All active facultative category with at least one
        active cookie, prefetch the cookie object
        Avoid circular import using get_model
        """
        Cookie = apps.get_model(app_label='gdpr_tools', model_name='Cookie')
        return self.get_facultative_categories().prefetch_related(
            Prefetch('cookies', queryset=Cookie.objects.filter(active=True))
        )
