from functools import wraps

from .models import Category, Consent
from .views import cookie_consent
from .utils import get_ip


def cookie_consent_decorator(view_func):
    """
    For every Cookie Category make sure the user has given consent
    if not redirect to the cookie consent view
    """
    def wrap(request, *args, **kwargs):
        ip = get_ip(request)
        consent = Consent.objects.filter(ip=ip)
        if not consent:
            return_url = request.build_absolute_uri()
            return cookie_consent(request, return_url)
        return view_func(request, *args, **kwargs)
    return wrap
