from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.http import is_safe_url

from .forms import ConsentForm


def cookie_consent(request, return_url):
    if request.method == "POST":
        form = ConsentForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            url_is_safe = is_safe_url(
                url=return_url,
                allowed_hosts=request.get_host(),
                require_https=request.is_secure(),
            )
            if url_is_safe:
                return HttpResponseRedirect(return_url)
        else:
            print('form not valid')
    else:
        form = ConsentForm()
    context = {
        'form': form
    }
    return render(
        request,
        'gdpr_tools/cookie_page.html',
        context=context
    )
