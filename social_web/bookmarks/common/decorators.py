from django.http import HttpResponseBadRequest





def ajax_required(func):
    def wraps(request, *args, **kwargs):
        def is_ajax(_request):
            return _request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

        if not is_ajax(request):
            return HttpResponseBadRequest()
        return func(request, *args, **kwargs)
    wraps.__doc__ = func.__doc__
    wraps.__name__ = func.__name__

    return wraps
