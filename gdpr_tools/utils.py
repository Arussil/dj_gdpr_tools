

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if not x_forwarded_for:
        return request.META.get('REMOTE_ADDR')
    return x_forwarded_for.split(',')[-1].strip()
